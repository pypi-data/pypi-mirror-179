"""Command line interface."""

import os
import sys
import json
import requests
import dotenv
import typer
from pydantic.error_wrappers import ValidationError
from workcell.utils.export import ExportFormat
from workcell.core import Workcell


# Add the current working directory to the sys path
# This is required to resolve the workcell path
sys.path.append(os.getcwd())
dotenv_file = os.path.join(os.getcwd(), ".weanalyze")
dotenv.load_dotenv(dotenv_file)
WORKCELL_GATEWAY = os.getenv("WORKCELL_GATEWAY", "https://fun.weanalyze.co")

# Typer command
cli = typer.Typer()


@cli.command()
def call(workcell_path: str, input_data: str) -> None:
    """Execute the workcell from command line."""
    
    # Add the current working directory to the sys path
    # This is required to resolve the workcell path
    sys.path.append(os.getcwd())
    try:
        output = Workcell(workcell_path)(input_data)
        if output:
            typer.echo(output.json(indent=4))
        else:
            typer.echo("Nothing returned!")
    except ValidationError as ex:
        typer.secho(str(ex), fg=typer.colors.RED, err=True)
    return None


@cli.command()
def serve(
    workcell_path: str,
    port: int = typer.Option(8080, "--port", "-p"),
    host: str = typer.Option("0.0.0.0", "--host", "-h"),
) -> None:
    """Start a HTTP API server for the workcell.

    This will launch a FastAPI server based on the OpenAPI standard and with a automatic interactive documentation.
    """
    # Add the current working directory to the sys path
    # This is required to resolve the workcell path
    sys.path.append(os.getcwd())
    from workcell.api.fastapi_app import launch_api  # type: ignore
    launch_api(workcell_path, port, host)
    return None


@cli.command()
def login(
    username: str = typer.Option("", "--username", "-u"),
    password: str = typer.Option("", "--password", "-p"),
) -> None:
    """Login into fun.weanalyze.co."""
    
    # Add the current working directory to the sys path
    # This is required to resolve the workcell path

    # Verification
    try:    
        if ('WORKCELL_TOKEN' in os.environ) and (os.getenv("WORKCELL_TOKEN") != ""):
            typer.secho("Already logged in ! (username: {})".format(os.environ['WORKCELL_USERNAME']), fg=typer.colors.GREEN, err=False)
            return None
        else:
            if (username == "") and (password == ""):
                typer.secho("Please provide username and password.", fg=typer.colors.RED, err=True)
                return None
            elif password == "":
                password = typer.prompt("Password", hide_input=True)
                # login params
                headers = {'Content-Type': 'application/x-www-form-urlencoded'}            
                data = {
                    'username': username,
                    'password': password
                } 
                # login url
                url = WORKCELL_GATEWAY + "/user/token"
                # login request   
                response = requests.post(url=url, data=data, headers=headers)
                if response.status_code == 200:
                    # extract token
                    token_value = response.json()["access_token"]
                    dotenv.set_key(dotenv_file, "WORKCELL_USERNAME", username)
                    dotenv.set_key(dotenv_file, "WORKCELL_TOKEN", token_value)
                    typer.echo("Login successful! (username: {}).".format(username))
                else:
                    typer.echo("Login failed! ({}).".format(response.text), fg=typer.colors.RED, err=True) 
            else:
                pass
    except ValidationError as ex:
        typer.secho(str(ex), fg=typer.colors.RED, err=True)
    return None


@cli.command()
def list() -> None:
    """List all workcell in weanalyze cloud.

    """
    # Add the current working directory to the sys path
    # This is required to resolve the workcell path
    sys.path.append(os.getcwd())
    # Verification
    try:    
        if ('WORKCELL_TOKEN' in os.environ) and (os.getenv("WORKCELL_TOKEN") != ""):
            # auth params
            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(os.getenv("WORKCELL_TOKEN")),
            } 
            # auth url 
            url = WORKCELL_GATEWAY + "/{}/list".format(os.getenv("WORKCELL_USERNAME"))
            # request 
            response = requests.get(url=url, headers=headers)
            # parse 
            result = response.json()
            typer.echo("{}".format(result['message']['stdout']))
        else:
            typer.secho("Login required!", fg=typer.colors.RED, err=True)
    except ValidationError as ex:
        typer.secho(str(ex), fg=typer.colors.RED, err=True)


@cli.command()
def pack(
    workcell_path: str,
    workcell_version: str = typer.Option("latest", "--version", "-v"),
    workcell_template: str = typer.Option("python3-workcell", "--template", "-t")
) -> str:
    """Prepare template folder for workcell.
    This will create a folder and package template in build_path.
    Args:
        workcell_path (str): path to workcell.
            e.g. workcell_path = "./examples/hello_workcell"
        workcell_version (str): workcell version.
            e.g. workcell_version = "latest"
        workcell_template (str): workcell template.
            e.g. workcell_template = "python3-workcell"
    Return:
        build_dir (str): path to build_dir.
        workcell_config (dict): dict of build config.
    """
    from workcell.utils.builder import copy_builder, tar_builder
    from workcell.utils.gen_config import gen_workcell_config
    workcell_config = gen_workcell_config(
        workcell_path,
        workcell_version,
        workcell_template
    )
    # copy from template and function
    files_path = os.path.join(os.getcwd(), *workcell_config['workcell_path'].split(":")[0].split(".")[:-1]) # "./examples/hello_world"
    build_dir = os.path.join(os.getcwd(), "build") # "./build"
    copy_builder(
        src = files_path, 
        dest = build_dir
    )
    # call tar builder
    tar_builder(
        src = build_dir, 
        dest = os.path.join(build_dir, 'tmp.tar.gz'),
        build_config = workcell_config
    )
    typer.secho("Workcell package complete!", fg=typer.colors.GREEN)
    return build_dir, workcell_config


@cli.command()
def build(
    workcell_path: str,
    workcell_version: str = typer.Option("latest", "--version", "-v"),
    workcell_template: str = typer.Option("python3-workcell", "--template", "-t")
) -> str:
    """Prepare template folder and build docker image for workcell.
    This will create a folder and package template in build_path, then build workcell docker image.
    Args:
        workcell_path (str): path to workcell.
            e.g. workcell_path = "./examples/hello_workcell"
        workcell_version (str): workcell version.
            e.g. workcell_version = "latest"
        workcell_template (str): workcell template.
            e.g. workcell_template = "python3-workcell"
    Return:
        build_dir (str): path to build_dir.
        workcell_config (dict): dict of build config.
    """
    from workcell.utils.builder import image_builder, image_pusher
    # copy from template and function
    build_dir, workcell_config = pack(
        workcell_path = workcell_path,
        workcell_version = workcell_version,
        workcell_template = workcell_template
    )
    build_path = os.path.join(build_dir, "workcell") # "./build/workcell"
    # call docker builder
    image_builder(
        src = build_path,
        tags = workcell_config['workcell_tags']
    )
    typer.secho("Docker image build finished, now start pushing...", fg=typer.colors.GREEN)
    image_pusher(
        repository = workcell_config['workcell_tags']
    )
    typer.secho("Docker image push finished.", fg=typer.colors.GREEN)
    typer.secho("Workcell build complete!", fg=typer.colors.GREEN)
    return build_dir, workcell_config


@cli.command()
def deploy(
    workcell_path: str,
    workcell_version: str = typer.Option("latest", "--version", "-v"),
    workcell_template: str = typer.Option("python3-workcell", "--template", "-t"), 
) -> None:
    """Deploy a workcell to weanalyze cloud.
    This will deploy a workcell to weanalyze cloud.
    Args:
        workcell_path (str): path to workcell.
            e.g. workcell_path = "./examples/hello_workcell"
        workcell_version (str): workcell version.
            e.g. workcell_version = "latest"
        workcell_template (str): workcell template.
            e.g. workcell_template = "python3-workcell"
    Return:
        None.
    """
    # Add the current working directory to the sys path
    # This is required to resolve the workcell path
    sys.path.append(os.getcwd())
    # Verification
    try:    
        if ('WORKCELL_TOKEN' in os.environ) and (os.getenv("WORKCELL_TOKEN") != ""):
            # build 
            build_dir, workcell_config = pack(
                workcell_path,
                workcell_version,
                workcell_template
            )
            # auth params
            headers = {
                "Authorization": "Bearer {}".format(os.getenv("WORKCELL_TOKEN")),
            } 
            # auth url 
            url = WORKCELL_GATEWAY + "/{}/deploy".format(os.getenv("WORKCELL_USERNAME"))            
            # post package to weanalyze cloud
            tar_file = os.path.join(build_dir,'tmp.tar.gz')
            with open(tar_file, "rb") as f:
                # request    
                response = requests.post(
                    url=url, 
                    headers=headers, 
                    data={'workcell_config':json.dumps(workcell_config)},
                    files={"workcell_tarfile": f}
                )
            # parse 
            try:
                result = response.json()
                typer.echo("Workcell status: {}".format(response.text))
            except:
                result = {"status": "error", "message": response.text}
                typer.echo("Workcell deploy failed! {}".format(result))
        else:
            typer.secho("Login required!", fg=typer.colors.RED, err=True)
    except ValidationError as ex:
        typer.secho(str(ex), fg=typer.colors.RED, err=True)
    

@cli.command()
def export(
    workcell_path: str, export_name: str, format: ExportFormat = ExportFormat.ZIP
) -> None:
    """Package and export a workcell."""
    if format == ExportFormat.ZIP:
        typer.secho(
            "[WIP] This feature is not finalized yet. You can track the progress and vote for the feature here: ",
            fg=typer.colors.BRIGHT_YELLOW,
        )
    elif format == ExportFormat.DOCKER:
        typer.secho(
            "[WIP] This feature is not finalized yet. You can track the progress and vote for the feature here: ",
            fg=typer.colors.BRIGHT_YELLOW,
        )
    elif format == ExportFormat.WE:
        typer.secho(
            "[WIP] This feature is not finalized yet. You can track the progress and vote for the feature here: ",
            fg=typer.colors.BRIGHT_YELLOW,
        )


if __name__ == "__main__":
    cli()
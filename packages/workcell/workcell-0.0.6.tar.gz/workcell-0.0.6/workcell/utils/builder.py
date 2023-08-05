import argparse
import subprocess
import hmac
import json
import os
import shutil
import tarfile
import click
import docker
from docker import APIClient

# TEMPLATE_FOLDER = "../thirdparty/openfaas/template"
WORKCELL_FOLDER =  os.path.abspath(os.path.join(__file__ , "../.."))
TEMPLATE_FOLDER = os.path.join(WORKCELL_FOLDER, "thirdparty/openfaas/template")


def copy_builder(src: str, dest: str) -> None:
    """Wrap user function in template

    Args:
        src (str): path to user defined function.
            e.g. func_path = "./examples/hello-workcell"
        dest (str): path to wrap user function into build folder.
            e.g. build_dir = "./build"

    Returns:
        None: mkdir for builder folder.    
    """
    if not os.path.exists(dest):
        os.makedirs(dest)
    else:
        shutil.rmtree(dest)
        os.makedirs(dest)
    try:
        template_path = os.path.join(TEMPLATE_FOLDER, "python3-workcell")
        # copy template
        #shutil.copytree(template_path, os.path.join(dest, os.path.basename(src)), symlinks=False, ignore=None, ignore_dangling_symlinks=False, dirs_exist_ok=True)
        #shutil.copytree(src, os.path.join(dest, os.path.basename(src), "function"), symlinks=False, ignore=None, ignore_dangling_symlinks=False, dirs_exist_ok=True)
        shutil.copytree(template_path, os.path.join(dest, "workcell"), symlinks=False, ignore=None, ignore_dangling_symlinks=False, dirs_exist_ok=True)
        shutil.copytree(src, os.path.join(dest, "workcell", "function"), symlinks=False, ignore=None, ignore_dangling_symlinks=False, dirs_exist_ok=True)
    except Exception as e:
        raise Exception("Copy builder failed! {}".format(e))


def image_builder(src: str, tags: str, client: APIClient = None) -> None:
    """Wrap user function in template

    Args:
        src (str): path contains Dockerfile to wrap user function into build folder.
            e.g. build_path = "./build/hello-workcell"
        tags (str): image tag.
            e.g. tags = "workcell:latest"

    Returns:
        None: docker images.
    """
    # check docker client
    if client is None:
        # client = docker.from_env()
        client = docker.APIClient()
    # docker build path
    click.echo("Building docker path: {}".format(src))
    log_generator = client.build(path=src, tag=tags, decode=True)
    log_docker_output(log_generator, "Build workcell docker image: {}".format(tags))


def image_pusher(repository: str, client: APIClient = None) -> None:
    """Push docker image to docker hub
    """
    # check docker client
    if client is None:
        # client = docker.from_env()
        client = docker.APIClient()
    # docker push
    log_generator = client.push(repository=repository, stream=True, decode=True)
    log_docker_output(log_generator, "Pushing workcell docker image to docker hub: {}".format(repository))


def tar_builder(src: str, dest: str, build_config: str = None) -> None:
    """Wrap user function in template

    Args:
        src (str): path to wrap user function into build folder.
            e.g. build_dir = "./build"
        dest (str): path to a tmp tar file.
            e.g. tar_file = "./build/tmp.tar.gz"
        build_config (dict): building configurations. 
            e.g. build_config = {
                    "workcell_name": workcell_name,
                    "workcell_version": workcell_version,
                    "workcell_template": workcell_template,
                    "workcell_tags": workcell_tags,
                    "workcell_env": ""
                } 
    Returns:
        None: _description_
    """
    config_file = os.path.join(src, 'workcell.json')
    with open(config_file, 'w') as f:
        json.dump(build_config, f, indent=4)

    with tarfile.open(dest, 'w') as tar:
        # tar.add(config_file, arcname='workcell.json')
        tar.add(src, arcname="build")


def log_docker_output(generator, task_name: str = 'docker command execution') -> None:
    """
    Log output to console from a generator returned from docker client
    :param Any generator: The generator to log the output of
    :param str task_name: A name to give the task, i.e. 'Build database image', used for logging
    """
    while True:
        try:
            output = generator.__next__()
            if 'stream' in output:
                if output['stream'] != '\n':
                    output_str = output['stream'].strip('\r\n').strip('\n')
                    click.echo(output_str)
        except StopIteration:
            click.echo(f'{task_name} complete.')
            break
        except ValueError:
            click.echo(f'Error parsing output from {task_name}: {output}')
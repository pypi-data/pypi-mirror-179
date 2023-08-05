import os
from workcell.core import Workcell, format_workcell_path, format_workcell_name

def gen_workcell_config(
    workcell_path: str,
    workcell_version: str,
    workcell_template: str
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
        workcell_config (dict): build config for workcell.
    """
    # extract workcell_config
    try:
        username = os.environ["WORKCELL_USERNAME"]
        workcell_path = format_workcell_path(workcell_path)
        workcell_version = workcell_version
        workcell_name = format_workcell_name(workcell_path)
        workcell_tags = "{}/{}:{}".format(username, workcell_name, workcell_version) # default build tag: {username}/{function_name}:{function_version}
    except:
        raise ValueError("The provided workcell_path is not callable.")
    # pack config
    workcell_config = {
        "workcell_name": workcell_name,
        "workcell_version": workcell_version,
        "workcell_template": workcell_template,
        "workcell_tags": workcell_tags,
        "workcell_env": "",
        "workcell_path": workcell_path
    }     
    return workcell_config
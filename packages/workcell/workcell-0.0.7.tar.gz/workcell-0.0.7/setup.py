# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['workcell',
 'workcell.api',
 'workcell.cli',
 'workcell.components',
 'workcell.core',
 'workcell.thirdparty.openfaas.template.python3-debian',
 'workcell.thirdparty.openfaas.template.python3-debian.function',
 'workcell.thirdparty.openfaas.template.python3-workcell',
 'workcell.thirdparty.openfaas.template.scipy-notebook',
 'workcell.thirdparty.openfaas.workcell',
 'workcell.utils']

package_data = \
{'': ['*'], 'workcell': ['thirdparty/openfaas/*']}

install_requires = \
['docker>=6.0.0,<7.0.0',
 'fastapi>=0.85.1,<0.86.0',
 'pydantic>=1.10.2,<2.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'typer>=0.3.1,<0.4.0',
 'uvicorn>=0.18.3,<0.19.0']

entry_points = \
{'console_scripts': ['workcell = workcell.cli:cli']}

setup_kwargs = {
    'name': 'workcell',
    'version': '0.0.7',
    'description': 'Turn python function into microservice.',
    'long_description': '<!-- markdownlint-disable MD033 MD041 -->\n<h1 align="center">\n    Workcell\n</h1>\n\n<p align="center">\n    <strong>Instantly turn your Python function into production-ready microservice.</strong>\n</p>\n\n<p align="center">\n    <a href="https://pypi.org/project/workcell/" title="PyPi Version"><img src="https://img.shields.io/pypi/v/workcell?color=green&style=flat"></a>\n    <a href="https://pypi.org/project/workcell/" title="Python Version"><img src="https://img.shields.io/badge/Python-3.8%2B-blue&style=flat"></a>\n    <a href="https://github.com/weanalyze/orpyter/blob/main/LICENSE" title="Project License"><img src="https://img.shields.io/badge/License-Apache2.0-blue.svg"></a>\n</p>\n\n<p align="center">\n  <a href="#getting-started">Getting Started</a> •\n  <a href="#license">License</a> •\n  <a href="https://github.com/weanalyze/orpyter/releases">Changelog</a>\n</p>\n\nInstantly turn your Python function into production-ready microservice. \n\n<sup>Pre-alpha Version: Not feature-complete and only suggested for experimental usage.</sup>\n\n<img align="center" style="width: 100%" src="https://github.com/weanalyze/weanalyze-resources/blob/main/assets/workcell_intro.png?raw=true"/>\n\n---\n\n## Highlights\n\n- 🪄&nbsp; Turn functions into production-ready services within seconds.\n- 🔌&nbsp; Auto-generated HTTP API based on FastAPI.\n- 📦&nbsp; Deploy microservice into weanalye FaaS cloud.\n- 🧩&nbsp; Reuse pre-defined templates & combine with existing components.\n- 📈&nbsp; Instantly deploy and scale for production usage.\n\n## Getting Started\n\n### Installation\n\n> _Requirements: Python 3.8+._\n\n```bash\npip install workcell\n```\n\n### Usage\n\n1. A simple orpyter-compatible function could look like this:\n\n    ```python\n    from pydantic import BaseModel\n\n    class Input(BaseModel):\n        message: str\n\n    class Output(BaseModel):\n        message: str\n\n    def main(input: Input) -> Output:\n        """Returns the `message` of the input data."""\n        return Output(message=input.message)\n    ```\n\n    _💡 A workcell-compatible function is required to have an `input` parameter and return value based on [Pydantic models](https://pydantic-docs.helpmanual.io/). The input and output models are specified via [type hints](https://docs.python.org/3/library/typing.html)._\n\n2. Copy this code to a file named `app.py`, put into a folder named as your function name, e.g. `hello-workcell`\n3. Run the HTTP API server from command-line:\n\n    ```bash\n    workcell serve ./hello-workcell/app.py\n    ```\n    _In the output, there\'s a line that shows where your  serverless funtion is being served, on your local machine._\n4. Deploy the service into weanalyze cloud from command-line:\n\n    ```bash\n    workcell login -u $USERNAME\n    workcell deploy ./hello-workcell/app.py\n    ```\n    _In the output, there\'s a line that shows where your web service is being served, on weanalyze cloud._\n5. Find out more usage information in the [Features](#features) section or get inspired by our [examples](#examples).\n\n## License\n\nApache-2.0 License.\n',
    'author': 'jiandong',
    'author_email': 'jiandong@weanalyze.co',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['compose_companion']

package_data = \
{'': ['*']}

install_requires = \
['python-dotenv>=0.21.0,<0.22.0',
 'pyyaml>=6.0,<7.0',
 'rich>=12.6.0,<13.0.0',
 'typer>=0.7.0,<0.8.0',
 'yaml-env-var-parser>=1.1.1,<2.0.0']

entry_points = \
{'console_scripts': ['compose = compose_companion.cli:app']}

setup_kwargs = {
    'name': 'compose-companion',
    'version': '0.2.1',
    'description': 'A companion for Docker Compose',
    'long_description': "# Compose Companion\n\nThis is a little CLI tool created for my home server.\n\nIt aims to make it easy to configure and document scripts that should run before and/or after the server containers on docker compose go up or down.\n\n## Scrips File\n\nThe app will read the scripts from a yaml file in the following format:\n\n```yaml\n# compose-companion.yaml\n\nx-before-up:\n  sonarr:\n    - echo this will run before sonarr startup\n    - echo this too will run before sonarr startup, after the previous one\n  radarr:\n    - echo this will run before radarr startup\n    - echo this too will run before radarr startup, after the previous one\n\nx-after-up:\n  sonarr:\n    - echo this will run after sonarr startup\n    - echo this too will run after sonarr startup, after the previous one\n  radarr:\n    - echo this will run after radarr startup\n    - echo this too will run after radarr startup, after the previous one\n\nx-before-down:\n  sonarr:\n    - echo this will run before sonarr shutdown\n    - echo this too will run before sonarr shutdown, after the previous one\n  radarr:\n    - echo this will run before radarr shutdown\n    - echo this too will run before radarr shutdown, after the previous one\n\nx-after-down:\n  sonarr:\n    - echo this will run after sonarr shutdown\n    - echo this too will run after sonarr shutdown, after the previous one\n  radarr:\n    - echo this will run after radarr shutdown\n    - echo this too will run after radarr shutdown, after the previous one\n```\n\nThe container keys should match the ones from `docker-compose.yaml` file.  \nThe app will look for a file named `compose-companion.yaml` on the folder it's first run, if that's not there it'll ask you to inform the file path manually.  \nAs the top-level keys start with `x-`, you can use the `docker-compose.yaml` file itself, if you wish, and these settings will be properly ignored by docker compose.  \n\n## Commands\n\nFor a list of command, run `compose --help` or simply `compose`.  \nFor details on each command, run `compose [command] --help`.\n",
    'author': 'Natália Fonseca',
    'author_email': 'natalia@nataliafonseca.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)

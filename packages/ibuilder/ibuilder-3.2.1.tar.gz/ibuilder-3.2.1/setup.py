# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ibuilder', 'ibuilder.config']

package_data = \
{'': ['*']}

install_requires = \
['arrow>=1.2.3,<2.0.0',
 'click>=8.1.3,<9.0.0',
 'docker>=6.0.0,<7.0.0',
 'packaging>=21.3,<22.0',
 'pydantic>=1.10.2,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'rich>=12.6.1,<13.0.0',
 'tinydb>=4.7.0,<5.0.0',
 'tomli>=2.0.1,<3.0.0',
 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['ib = ibuilder.main:app']}

setup_kwargs = {
    'name': 'ibuilder',
    'version': '3.2.1',
    'description': 'build, tag, push, and sign docker images',
    'long_description': '# README\n\nibuilder is a [cli](https://en.wikipedia.org/wiki/Command-line_interface) based builder of [docker](https://hub.docker.com/) images. It provides an interface for building and pushing the image, signing images, as well as for tagging source code after build with a build version and other common image tasks.\n\n### New\n\n- add ability to sign on repush\n- upgrade packages (arrow, docker, pydantic, requests, rich, and typer)\n\n### Features\n\n- build: build docker images\n- push: push images to any container registry\n- sign: sign images for container signing and verification\n- source control: tag and push when you build an image\n- history: retain build history for quick/easy access to past build info\n- quick/easy: create an `ibuilder.toml` file and run `ib build -i minor` to build, push, commit to source control and sign a new image\n\n### Requirements\n\n- python 3\n- docker: docker must be set up as it is used to build and push the image\n- git: (optional) if you use the source-tag feature you will need git installed and your code setup in git (it simply performs a git tag && git push from the working directory)\n- image signor: (optional) if you choose to sign images a signor (such as cosign) is needed\n\n### Overview\n\n- setup (see #setup)\n- configure (see #configure): place a copy of the `example/.ibuilder.toml` in the same directory as your Dockerfile of the app you want to build and adjust it as needed\n- run (see #run): execute ibuilder to build/push/tag a version of your app, its as simple as `ib build`\n\n\n### Install\n\nWe recommend using [pipx](https://github.com/pypa/pipx) to install ibuilder: `pipx install ibuilder`. You can also install via pip: `pip install --user ibuilder`.\n\n\n### Setup\n\nibuilder uses a config file to store your setup. Each \'app\' you build with ibuilder expects this file to be in the \'root\' of the app that you are building. This file contains information such as whether to build, push, tag the image, labels to apply, Dockerfile to use, etc. You can grab an example config file from  [ibuilder/example/.ibuilder.toml](https://gitlab.com/drad/ibuilder/-/blob/master/example/.ibuilder.toml).\n\n\n### Configure\n\n- create a project config file\n  - place a copy of the `example/.ibuilder.toml` file in your project (same directory as your Dockerfile) and configure as needed\n\n\n### Features\n\nIf you create an arg with the name "BUILD_VERSION" its value will be replaced with the build version of the current build. This can be used to pass the build version from ibuilder into your docker environment.\n\n\n### Run\n\n- basic run: `ib build --version=1.2.3`\n  - the above command assumes there is a `.ibuilder.toml` in the current working directory which happens to be in the same directory as the Dockerfile which you wish to build\n- change logging level: `LOG_LEVEL=DEBUG ib build...`\n  + standard python log levels supported: CRITICAL|ERROR|WARNING|INFO|DEBUG (default is INFO)\nView help with `ib --help` or see help for a specific command: `ib build --help`.\n\n\n### Recommendations\n\nWe recommend using docker\'s configuration storage for reg_auth-* related configuration items as it encrypts sensitive information and is likely already configured (if you have already used `docker login`). If you leave the remaining items empty the default values will be used. This will then try `$HOME/.docker/config.json` and `$HOME/.dockercfg` for your docker config settings. If you do not already have a docker config run `docker login` and it should be created for you. After a successful login you should not need to do anything else for the application as the needed info will be stored in your dockercfg and the app will use it when needed.\n\nIf you are signing your images you may want to set the `COSIGN_PASSWORD` environment variable in your `~/.bashrc` or equivalent shell config file to avoid being prompted for your signing password after build and push. It should be noted that you will be prompted twice (if you are pushing both the build version and the `latest` tag of this version) as ib signs both tags of the built image. To avoid this we recommend setting the `COSIGN_PASSWORD` environment variable but please ensure you understand the security implications of doing so.\n\n### Legacy\n\nThis project originally started under the name boi - builder of images and as such you may find references to boi and even backward support for boi (e.g. local history database, user config file, etc.).\n\n\n### Links\n\n- [typer](https://typer.tiangolo.com/)\n- [docker](https://pypi.org/project/docker/)\n  - [docs](https://docker-py.readthedocs.io/en/stable/)\n- [toml](https://pypi.org/project/toml/)',
    'author': 'David Rader',
    'author_email': 'sa@adercon.com',
    'maintainer': 'David Rader',
    'maintainer_email': 'sa@adercon.com',
    'url': 'https://gitlab.com/drad/ibuilder',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

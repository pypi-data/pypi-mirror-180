# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['skate', 'skate.config', 'skate.screens']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['skate = skate.cli:skate']}

setup_kwargs = {
    'name': 'skate',
    'version': '0.0.2',
    'description': 'Organize and run frequently used commands',
    'long_description': '# skate\n\n[![Release](https://img.shields.io/github/v/release/fpgmaas/skate)](https://img.shields.io/github/v/release/fpgmaas/skate)\n[![Build status](https://img.shields.io/github/workflow/status/fpgmaas/skate/Main/main)](https://github.com/fpgmaas/skate/actions/workflows/main.yml?query=branch%3Amain)\n[![codecov](https://codecov.io/gh/fpgmaas/skate/branch/main/graph/badge.svg)](https://codecov.io/gh/fpgmaas/skate)\n[![Commit activity](https://img.shields.io/github/commit-activity/m/fpgmaas/skate)](https://img.shields.io/github/commit-activity/m/fpgmaas/skate)\n[![License](https://img.shields.io/github/license/fpgmaas/skate)](https://img.shields.io/github/license/fpgmaas/skate)\n\nOrganize and run frequently used commands\n\n- **Github repository**: <https://github.com/fpgmaas/skate/>\n- **Documentation** <https://fpgmaas.github.io/skate/>\n\n## Getting started with your project\n\nFirst, create a repository on GitHub with the same name as this project, and then run the following commands:\n\n``` bash\ngit init -b main\ngit add .\ngit commit -m "init commit"\ngit remote add origin git@github.com:fpgmaas/skate.git\ngit push -u origin main\n```\n\nFinally, install the environment and the pre-commit hooks with \n\n```bash\nmake install\n```\n\nYou are now ready to start development on your project! The CI/CD\npipeline will be triggered when you open a pull request, merge to main,\nor when you create a new release.\n\nTo finalize the set-up for publishing to PyPi or Artifactory, see\n[here](https://fpgmaas.github.io/cookiecutter-poetry/features/publishing/#set-up-for-pypi).\nFor activating the automatic documentation with MkDocs, see\n[here](https://fpgmaas.github.io/cookiecutter-poetry/features/mkdocs/#enabling-the-documentation-on-github).\nTo enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/codecov/).\n\n## Releasing a new version\n\n- Create an API Token on [Pypi](https://pypi.org/).\n- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting \n[this page](https://github.com/fpgmaas/skate/settings/secrets/actions/new).\n- Create a [new release](https://github.com/fpgmaas/skate/releases/new) on Github. \nCreate a new tag in the form ``*.*.*``.\n\nFor more details, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/cicd/#how-to-trigger-a-release).\n\n---\n\nRepository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).',
    'author': 'Florian Maas',
    'author_email': 'ffpgmaas@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/fpgmaas/skate',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<=3.11',
}


setup(**setup_kwargs)

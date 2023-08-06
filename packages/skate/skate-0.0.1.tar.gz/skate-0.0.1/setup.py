# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clitools', 'clitools.config', 'clitools.screens']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'keyboard>=0.13.5,<0.14.0', 'pyyaml>=6.0,<7.0']

entry_points = \
{'console_scripts': ['clitools = clitools.cli:clitools']}

setup_kwargs = {
    'name': 'skate',
    'version': '0.0.1',
    'description': 'Test project',
    'long_description': '# clitools\n\n[![Release](https://img.shields.io/github/v/release/fpgmaas/clitools)](https://img.shields.io/github/v/release/fpgmaas/clitools)\n[![Build status](https://img.shields.io/github/workflow/status/fpgmaas/clitools/Main/main)](https://github.com/fpgmaas/clitools/actions/workflows/main.yml?query=branch%3Amain)\n[![codecov](https://codecov.io/gh/fpgmaas/clitools/branch/main/graph/badge.svg)](https://codecov.io/gh/fpgmaas/clitools)\n[![Commit activity](https://img.shields.io/github/commit-activity/m/fpgmaas/clitools)](https://img.shields.io/github/commit-activity/m/fpgmaas/clitools)\n[![License](https://img.shields.io/github/license/fpgmaas/clitools)](https://img.shields.io/github/license/fpgmaas/clitools)\n\nTest project\n\n- **Github repository**: <https://github.com/fpgmaas/clitools/>\n- **Documentation** <https://fpgmaas.github.io/clitools/>\n\n## Getting started with your project\n\nFirst, create a repository on GitHub with the same name as this project, and then run the following commands:\n\n``` bash\ngit init -b main\ngit add .\ngit commit -m "init commit"\ngit remote add origin git@github.com:fpgmaas/clitools.git\ngit push -u origin main\n```\n\nFinally, install the environment and the pre-commit hooks with \n\n```bash\nmake install\n```\n\nYou are now ready to start development on your project! The CI/CD\npipeline will be triggered when you open a pull request, merge to main,\nor when you create a new release.\n\nTo finalize the set-up for publishing to PyPi or Artifactory, see\n[here](https://fpgmaas.github.io/clitools/features/publishing/#set-up-for-pypi).\nFor activating the automatic documentation with MkDocs, see\n[here](https://fpgmaas.github.io/clitools/features/mkdocs/#enabling-the-documentation-on-github).\nTo enable the code coverage reports, see [here](https://fpgmaas.github.io/clitools/features/codecov/).\n\n## Releasing a new version\n\n\n\n---\n\nRepository initiated with [fpgmaas/clitools](https://github.com/fpgmaas/clitools).',
    'author': 'Florian Maas',
    'author_email': 'ffpgmaas@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/fpgmaas/clitools',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<=3.11',
}


setup(**setup_kwargs)

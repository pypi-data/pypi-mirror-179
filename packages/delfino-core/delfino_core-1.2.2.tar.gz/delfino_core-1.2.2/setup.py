# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['delfino_core', 'delfino_core.commands']

package_data = \
{'': ['*']}

install_requires = \
['delfino>=0.21.0']

extras_require = \
{'all': ['black',
         'isort',
         'pre-commit',
         'pytest',
         'coverage',
         'pytest-cov',
         'mypy',
         'pylint',
         'pycodestyle',
         'pydocstyle',
         'twine'],
 'format': ['black', 'isort', 'pre-commit'],
 'lint': ['pylint', 'pycodestyle', 'pydocstyle'],
 'test': ['pytest', 'coverage', 'pytest-cov'],
 'typecheck': ['mypy'],
 'upload-to-pypi': ['twine'],
 'verify-all': ['black',
                'isort',
                'pre-commit',
                'pytest',
                'coverage',
                'pytest-cov',
                'mypy',
                'pylint',
                'pycodestyle',
                'pydocstyle']}

entry_points = \
{'delfino.plugin': ['delfino-core = delfino_core.commands']}

setup_kwargs = {
    'name': 'delfino-core',
    'version': '1.2.2',
    'description': 'Delfino core plugin',
    'long_description': '<h1 align="center" style="border-bottom: none;"> 🔌&nbsp;&nbsp;Delfino Core&nbsp;&nbsp; 🔌</h1>\n<h3 align="center">A <a href="https://github.com/radeklat/delfino">Delfino</a> plugin with core functionality.</h3>\n\n<p align="center">\n    <a href="https://app.circleci.com/pipelines/github/radeklat/delfino-core?branch=main">\n        <img alt="CircleCI" src="https://img.shields.io/circleci/build/github/radeklat/delfino-core">\n    </a>\n    <a href="https://app.codecov.io/gh/radeklat/delfino-core/">\n        <img alt="Codecov" src="https://img.shields.io/codecov/c/github/radeklat/delfino-core">\n    </a>\n    <a href="https://github.com/radeklat/delfino-core/tags">\n        <img alt="GitHub tag (latest SemVer)" src="https://img.shields.io/github/tag/radeklat/delfino-core">\n    </a>\n    <img alt="Maintenance" src="https://img.shields.io/maintenance/yes/2022">\n    <a href="https://github.com/radeklat/delfino-core/commits/main">\n        <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/radeklat/delfino-core">\n    </a>\n    <a href="https://www.python.org/doc/versions/">\n        <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/delfino-core">\n    </a>\n    <a href="https://pypistats.org/packages/delfino-core">\n        <img alt="Downloads" src="https://img.shields.io/pypi/dm/delfino-core">\n    </a>\n</p>\n\n# Installation\n\n- pip: `pip install delfino-core`\n- Poetry: `poetry add -D delfino-core`\n- Pipenv: `pipenv install -d delfino-core`\n\n## Optional dependencies\n\nEach project may use different sub-set of commands. Therefore, dependencies of all commands are optional and checked only when the command is executed.\n\nUsing `[all]` installs all the [optional dependencies](https://setuptools.pypa.io/en/latest/userguide/dependency_management.html#optional-dependencies) used by all the commands. If you want only a sub-set of those dependencies, there are finer-grained groups available:\n\n- For individual commands (matches the command names):\n  - `upload_to_pypi`\n  - `build_docker`\n  - `typecheck`\n  - `format`\n- For groups of commands:\n  - `test` - for testing and coverage commands\n  - `lint` - for all the linting commands\n- For groups of groups:\n  - `verify_all` - same as `[typecheck,format,test,lint]`\n  - `all` - all optional packages\n\n## Configuration\n\nDelfino doesn\'t load any plugins by default. To enable this plugin, add the following config into `pyproject.toml`:\n\n```toml\n[tool.delfino.plugins.delfino-core]\n\n```\n\n# Usage\n\nRun `delfino --help`.\n\n# Development\n\nTo develop against editable `delfino` sources:\n\n1. Make sure `delfino` sources are next to this plugin:\n    ```shell\n    cd ..\n    git clone https://github.com/radeklat/delfino.git\n    ```\n2. Install `delfino` as editable package:\n    ```shell\n    pip install -e ../delfino\n    ```\n   Note that poetry will reset this to the released package when you install/update anything.\n',
    'author': 'Radek Lát',
    'author_email': 'radek.lat@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/radeklat/delfino-core',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)

# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['laureate']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'jinja2>=3.1.2,<4.0.0',
 'requests>=2.28.1,<3.0.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['laureate = laureate.laureate:cli']}

setup_kwargs = {
    'name': 'laureate',
    'version': '1.0.0',
    'description': 'Generate Homebrew formulae for Poetry projects',
    'long_description': '# laureate\n\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/laureate?logo=python&logoColor=white&style=for-the-badge)](https://pypi.org/project/laureate)\n[![PyPI](https://img.shields.io/pypi/v/laureate?logo=pypi&logoColor=white&style=for-the-badge)](https://pypi.org/project/laureate)\n[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/celsiusnarhwal/laureate?color=orange&label=latest%20release&logo=github&logoColor=white&style=for-the-badge)](https://github.com/celsiusnarhwal/laureate)\n[![PyPI - License](https://img.shields.io/pypi/l/laureate?color=03cb98&style=for-the-badge)](https://github.com/celsiusnarhwal/laureate/blob/HEAD/LICENSE.md)\n\n\n\n\nlaureate generates [Homebrew](https://brew.sh) formulae for Python projects that use [Poetry](https://python-poetry.org).\n\n## Installation\n\n```bash\npoetry add laureate\n```\n\n## Requirements\n\nlaureate can only generate formulae for packages that meet the following criteria:\n\n- The package must be published on PyPI.\n- `pyproject.toml` and `poetry.lock` must be present in the directory where laureate is run.\n- `pyproject.toml` must specify values for `tool.poetry.name`, `tool.poetry.version`,\n  and `tool.poetry.dependencies.python`.\n    - `tool.poetry.name` must be a case-insensitive match with the package\'s name on PyPI.\n    - `tool.poetry.version` must match a version of the package that has been published on PyPI.\n\n## Usage\n\n```\nUsage: laureate.py [OPTIONS]\n\n  Generate a Homebrew formula for a Poetry project.\n\nOptions:\n  -o, --output DIRECTORY  The directory to save the formula to. Defaults to the current directory.\n  -i, --include TEXT      A group to include.\n  -e, --exclude TEXT      A group to exclude.\n  --license               See Laureate\'s license.\n  --help                  Show this message and exit.\n```\n\nThe simplest usage is just:\n\n```bash\nlaureate\n```\n\nwhich will generate a complete formula for your project in the currrent directory with the name\n`<project-name>.rb`.\n\n### `--include` and `--exclude`\n\nIf you have multiple groups of dependencies specified in `pyproject.toml`, you can use `--include` and `--exclude` to\ncontrol which ones make it into the formula. By default, the `main` group (everything in `tool.poetry.dependencies`) is\nincluded and all other groups are excluded.\n\nNote that:\n- Groups specified in `--include` are included in *addition* to `main`. If you wish to exclude\n  `main`, you must do so explicitly with ``--exclude``.\n- ``--exclude`` takes precedence over ``--include``. Groups specificed in both will be excluded.\n\n#### Example Usage\n\n```bash\n# Include the "dev" group.\nlaureate --include dev\n\n# Include the "dev" and "docs" groups.\nlaureate --include dev --include docs\n\n# Include the "dev" and "docs" groups, but exclude "main".\nlaureate --include dev --include docs --exclude main\n```\n\n\n## Differences from homebrew-pypi-poet\n\nlaureate pulls information about your package and its dependencies directly from `pyproject.toml`, `poetry.lock`, and\nPyPI, eliminating the need to first install your package and its dependencies in a virtual environment before generating\nthe formula. For generating complete formulae, laurate is far faster and easier to use than homebrew-pypi-poet for this\nreason alone.\n\nHowever, laureate is also far less featured than homebrew-pypi-poet. It *only* supports generating complete formulae;\nhomebrew-pypi-poet can generate resource stanzas for individual packages and allows for the specification\nof additional packages to generate stanzas for at invocation time. laureate also strictly only works with Poetry\nprojects, whereas homebrew-pypi-poet does not care about your package manager of choice.\n\nlaureate was created to fill my own development needs and is being released in the hopes that others may find it useful.\nIf you require more flexibility than simply generating a complete Homebrew formula for a Poetry project, use\nhomebrew-pypi-poet.\n\n## License\n\nlaureate is licensed under the [MIT License](https://github.com/celsiusnarhwal/laureate/blob/HEAD/LICENSE.md).',
    'author': 'celsius narhwal',
    'author_email': 'hello@celsiusnarhwal.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/celsiusnarhwal/laureate',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

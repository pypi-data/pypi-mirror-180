# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['repoutil']

package_data = \
{'': ['*'], 'repoutil': ['gitignores/*', 'licenses/*', 'workflows/*']}

install_requires = \
['click>=8.0.1,<9.0.0']

entry_points = \
{'console_scripts': ['repo = repoutil.main:main']}

setup_kwargs = {
    'name': 'repoutil',
    'version': '0.1.0',
    'description': 'A simple command line utility to write gitignores, licenses and workflow files to a project.',
    'long_description': "# repoutil\n\nrepoutil is a simple command line utility to write gitignores, licenses and workflow files to a project.\n\n## Usage\n\n```\nUsage: repo [OPTIONS] COMMAND [ARGS]...\n\n  repo is a simple command line utility to write gitignores, licenses and\n  workflows to a repo.\n\nOptions:\n  --version  Show the version and exit.\n  --help     Show this message and exit.\n\nCommands:\n  g  Generates a gitignore file for the given language.\n  l  Generates a license file for the given license.\n  w  Generates a workflow file for the given language.\n```\n\nExamples:\n```\nrepo g python # generate a gitignore file for python\nrepo l mit # generate a mit license file\n```\n\n\n<br>\n\n\n## Versioning\n\nrepoutil releases follow semantic versioning, every release is in the *x.y.z* form, where:\n\n- x is the MAJOR version and is incremented when a backwards incompatible change to stella is made.\n- y is the MINOR version and is incremented when a backwards compatible change to stella is made, like changing dependencies or adding a new function, method, or features.\n- z is the PATCH version and is incremented after making minor changes that don't affect stella's public API or dependencies, like fixing a bug.\n\n<br>\n\n## Licensing\n\nLicense © 2021-Present Shravan Asati\n\nThis repository is licensed under the MIT license. See [LICENSE](LICENSE.txt) for details.",
    'author': 'Shravan Asati',
    'author_email': 'dev.shravan@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://bitbucket.org/shravannn/repoutil',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

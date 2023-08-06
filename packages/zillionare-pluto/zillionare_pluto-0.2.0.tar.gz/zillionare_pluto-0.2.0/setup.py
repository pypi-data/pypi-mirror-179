# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pluto',
 'pluto.config',
 'pluto.core',
 'pluto.store',
 'pluto.strategies',
 'pluto.tasks',
 'pluto.web',
 'pluto.web.handlers',
 'pluto.web.handlers.strategies',
 'tests',
 'tests.data.core',
 'tests.store',
 'tests.strategies']

package_data = \
{'': ['*'],
 'pluto.web': ['static/*', 'static/data/*', 'static/pages/*'],
 'tests': ['data/*']}

install_requires = \
['cfg4py>=0.9.4,<0.10.0',
 'fire==0.4.0',
 'freezegun>=1.2.2,<2.0.0',
 'pyemit>=0.5.0,<0.6.0',
 'zarr>=2.13.2,<3.0.0',
 'zillionare-core-types>=0.5.2,<0.6.0',
 'zillionare-omicron>=2.0.0a59,<3.0.0',
 'zillionare-ths-boards>=0.2,<0.3',
 'zillionare-trader-client>=0.3,<0.4']

extras_require = \
{'dev': ['tox>=3.24.5,<4.0.0',
         'virtualenv>=20.13.1,<21.0.0',
         'pip>=22.0.3,<23.0.0',
         'twine>=3.8.0,<4.0.0',
         'pre-commit>=2.17.0,<3.0.0',
         'toml>=0.10.2,<0.11.0'],
 'doc': ['mkdocs>=1.2.3,<2.0.0',
         'mkdocs-include-markdown-plugin>=3.2.3,<4.0.0',
         'mkdocs-material>=8.1.11,<9.0.0',
         'mkdocstrings>=0.18.0,<0.19.0',
         'mkdocs-autorefs>=0.3.1,<0.4.0',
         'mike>=1.1.2,<2.0.0'],
 'test': ['black>=22.3.0,<23.0.0',
          'isort==5.10.1',
          'flake8==4.0.1',
          'flake8-docstrings>=1.6.0,<2.0.0',
          'pytest>=7.0.1,<8.0.0',
          'pytest-cov>=3.0.0,<4.0.0']}

entry_points = \
{'console_scripts': ['pluto = pluto.cli:main']}

setup_kwargs = {
    'name': 'zillionare-pluto',
    'version': '0.2.0',
    'description': 'Skeleton project created by Python Project Wizard (ppw).',
    'long_description': '# pluto\n\n\n<p align="center">\n<a href="https://pypi.python.org/pypi/pluto">\n    <img src="https://img.shields.io/pypi/v/pluto.svg"\n        alt = "Release Status">\n</a>\n\n<a href="https://github.com/zillionare/pluto/actions">\n    <img src="https://github.com/zillionare/pluto/actions/workflows/main.yml/badge.svg?branch=release" alt="CI Status">\n</a>\n\n<a href="https://zillionare.github.io/pluto/">\n    <img src="https://img.shields.io/website/https/zillionare.github.io/pluto/index.html.svg?label=docs&down_message=unavailable&up_message=available" alt="Documentation Status">\n</a>\n\n</p>\n\n\nSkeleton project created by Python Project Wizard (ppw)\n\n\n* Free software: MIT\n* Documentation: <https://zillionare.github.io/pluto/>\n\n\n## Features\n\n* TODO\n\n## Credits\n\nThis package was created with the [ppw](https://zillionare.github.io/python-project-wizard) tool. For more information, please visit the [project page](https://zillionare.github.io/python-project-wizard/).\n',
    'author': 'aaron yang',
    'author_email': 'aaron_yang@jieyu.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/zillionare/pluto',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.9',
}


setup(**setup_kwargs)

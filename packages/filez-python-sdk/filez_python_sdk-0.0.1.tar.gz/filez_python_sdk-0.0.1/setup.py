# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['filez_python_sdk', 'tests']

package_data = \
{'': ['*']}

install_requires = \
['click==8.1.3']

entry_points = \
{'console_scripts': ['filez-python-sdk = filez_python_sdk.cli:main']}

setup_kwargs = {
    'name': 'filez-python-sdk',
    'version': '0.0.1',
    'description': 'Skeleton project created by Cookiecutter PyPackage.',
    'long_description': '<p align="center">\n    <a href="https://www.filez.com/">\n    <img src="https://raw.githubusercontent.com/wccdev/filez-python-sdk/master/.github/assets/logo-black.png" width="120" margin="50" alt="Python SDK For FileZ">\n    </a>\n</p>\n<p align="center">\n    <strong>\n    Python SDK for\n    <a href="https://www.filez.com/">Lenovo FileZ</a>\n    </strong>\n</p>\n<p align="center">\n    <a href="https://github.com/wccdev/filez-python-sdk/actions/workflows/ci.yml"><img\n        src="https://github.com/wccdev/filez-python-sdk/actions/workflows/ci.yml/badge.svg"\n        alt="Build"\n        /></a>\n    <a href="https://github.com/wccdev/filez-python-sdk/blob/main/LICENSE"><img\n        src="https://img.shields.io/github/license/wccdev/filez-python-sdk"\n        alt="License"\n        /></a>\n    <a href="https://pypi.org/project/filez-python-sdk/"><img\n        src="https://img.shields.io/pypi/pyversions/filez-python-sdk.svg"\n        alt="Python"\n        /></a>\n    <a href="https://pypi.org/project/filez-python-sdk/"><img\n        src="https://img.shields.io/pypi/v/filez-python-sdk.svg"\n        alt="Python Package Index"\n        /></a>\n    <a href="https://github.com/psf/black"><img\n        src="https://img.shields.io/badge/code%20style-black-000000.svg"\n        alt="Code Style"\n        /></a>\n</p>\n<p align="center">\n    Skeleton project created by Cookiecutter PyPackage.\n</p>\n<h2></h2>\n\n## Quick start\n\n* TODO\n\n\n## Features\n\n* TODO\n\n## Credits\n\nThis package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [wccdev/cookiecutter-pypackage](https://github.com/wccdev/cookiecutter-pypackage) project template.\n',
    'author': 'Aiden Lu',
    'author_email': 'allaher@icloud.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/wccdev/filez-python-sdk',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

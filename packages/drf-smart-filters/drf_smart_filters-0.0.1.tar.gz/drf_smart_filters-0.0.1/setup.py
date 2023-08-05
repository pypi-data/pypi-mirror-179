# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['drf_smart_filters', 'tests']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'drf-smart-filters',
    'version': '0.0.1',
    'description': 'Skeleton project created by Cookiecutter PyPackage.',
    'long_description': '# drf-smart-filters\n\n\n[![pypi](https://img.shields.io/pypi/v/drf-smart-filters.svg)](https://pypi.org/project/drf-smart-filters/)\n[![license](https://img.shields.io/github/license/wccdev/drf-smart-filters)](https://github.com/wccdev/drf-smart-filters/blob/main/LICENSE)\n[![python](https://img.shields.io/pypi/pyversions/drf-smart-filters.svg)](https://pypi.org/project/drf-smart-filters/)\n[![Build Status](https://github.com/wccdev/drf-smart-filters/actions/workflows/ci.yml/badge.svg)](https://github.com/wccdev/drf-smart-filters/actions/workflows/ci.yml)\n[![codecov](https://codecov.io/gh/wccdev/drf-smart-filters/branch/main/graphs/badge.svg)](https://codecov.io/github/wccdev/drf-smart-filters)\n[![Built with Cookiecutter Pypackage](https://img.shields.io/badge/built%20with-Cookiecutter%20Pypackage-ff69b4.svg?logo=cookiecutter)](https://github.com/wccdev/cookiecutter-pypackage)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n\n\n\nSkeleton project created by Cookiecutter PyPackage\n\n\n* Documentation: <https://wccdev.github.io/drf-smart-filters>\n* GitHub: <https://github.com/wccdev/drf-smart-filters>\n* PyPI: <https://pypi.org/project/drf-smart-filters/>\n* Free software: MIT\n\n\n## Features\n\n* TODO\n\n## Credits\n\nThis package was created with [Cookiecutter](https://github.com/wccdev/cookiecutter) and the [wccdev/cookiecutter-pypackage](https://github.com/wccdev/cookiecutter-pypackage) project template.\n',
    'author': 'Aiden Lu',
    'author_email': 'allaher@icloud.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/wccdev/drf-smart-filters',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

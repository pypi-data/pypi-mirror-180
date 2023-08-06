# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['sublate']
install_requires = \
['jinja2>=3.1.2,<4.0.0', 'pyyaml>=6.0,<7.0']

entry_points = \
{'console_scripts': ['sublate = sublate:main']}

setup_kwargs = {
    'name': 'sublate',
    'version': '0.3.1',
    'description': 'A high-level toolkit.',
    'long_description': 'None',
    'author': 'Jonathan Esposito',
    'author_email': 'jonathan@esposito.page',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

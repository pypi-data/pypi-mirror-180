# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['crdt']
entry_points = \
{'console_scripts': ['crdt = crdt:main']}

setup_kwargs = {
    'name': 'crdt',
    'version': '0.0.1',
    'description': 'Conflict-free Replicated Data Type tools',
    'long_description': 'None',
    'author': 'Angelo Gladding',
    'author_email': 'angelo@ragt.ag',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://ragt.ag/code/projects/python-crdt',
    'py_modules': modules,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)

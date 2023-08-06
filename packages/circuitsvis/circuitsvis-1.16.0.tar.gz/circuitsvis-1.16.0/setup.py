# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['circuitsvis',
 'circuitsvis.tests',
 'circuitsvis.tests.snapshots',
 'circuitsvis.utils',
 'circuitsvis.utils.tests',
 'circuitsvis.utils.tests.snapshots']

package_data = \
{'': ['*'], 'circuitsvis': ['dist/cdn/*']}

install_requires = \
['importlib-metadata>=5.1.0,<6.0.0', 'numpy>=1.20,<2.0']

setup_kwargs = {
    'name': 'circuitsvis',
    'version': '1.16.0',
    'description': 'Mechanistic Interpretability Visualizations',
    'long_description': '# Circuits Vis\n\nMechanistic Interpretability visualizations.\n',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

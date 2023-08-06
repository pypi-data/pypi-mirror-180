# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['s2b_task']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0', 'pytest>=7.2.0,<8.0.0']

entry_points = \
{'console_scripts': ['do_task = s2b_task.task_executor:do_task']}

setup_kwargs = {
    'name': 's2b-task',
    'version': '0.0.4',
    'description': 'Python tasks manager for python3.11',
    'long_description': 'None',
    'author': 'nixissmtp',
    'author_email': 'nixissmtp@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)

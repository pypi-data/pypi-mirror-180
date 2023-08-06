# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['killtimer']

package_data = \
{'': ['*']}

install_requires = \
['desktop-notifier>=3.4.0,<4.0.0',
 'humanfriendly>=10.0,<11.0',
 'just-playback>=0.1.7,<0.2.0',
 'pytimeparse>=1.1.8,<2.0.0',
 'rich>=12.4.3,<13.0.0']

entry_points = \
{'console_scripts': ['killtimer = killtimer.main:main',
                     'killtimer-stats = killtimer.stats:main']}

setup_kwargs = {
    'name': 'killtimer',
    'version': '0.2.0',
    'description': 'Closes application after specified work interval',
    'long_description': 'None',
    'author': 'Paweł Żukowski',
    'author_email': 'p.z.idlecode@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/idle-code/killtimer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

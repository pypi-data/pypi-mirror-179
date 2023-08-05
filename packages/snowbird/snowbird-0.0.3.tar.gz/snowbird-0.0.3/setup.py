# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['snowbird']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'click>=8.1.3,<9.0.0',
 'permifrost>=0.14.0,<0.15.0',
 'pydantic>=1.10.2,<2.0.0']

entry_points = \
{'console_scripts': ['snowbird = snowbird.command:cli']}

setup_kwargs = {
    'name': 'snowbird',
    'version': '0.0.3',
    'description': 'Snowbird helps configure Snowflake resources for dataproducts.',
    'long_description': "===============\n About\n===============\n\nSnowbird helps configure Snowflake resources for dataproducts. Snowbird builds on Permifrost.\n\n===============\n Installation\n===============\n\npip install snowbird\n\n===============\n Example\n===============\n\nThe default declaration file name is 'snowflake.yml' and the default location of the file is ./infrastructure\n\nIn this case you can simply run the command: $ snowbird run \n\n\n",
    'author': 'pbencze',
    'author_email': 'paul@idelab.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

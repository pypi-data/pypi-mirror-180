# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['awsdf']

package_data = \
{'': ['*']}

install_requires = \
['awswrangler>=2.14.0,<3.0.0',
 'loguru>=0.6.0,<0.7.0',
 'tabulate>=0.8.9,<0.9.0',
 'tqdm>=4.64.0,<5.0.0']

setup_kwargs = {
    'name': 'awsdf',
    'version': '0.1.6',
    'description': 'AWS metadata as dataframes',
    'long_description': '# AWS metadata as dataframes\n',
    'author': 'Allan',
    'author_email': 'allan.dsouza@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)

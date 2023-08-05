# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['private_reg']

package_data = \
{'': ['*']}

install_requires = \
['docker>=6.0.1,<7.0.0', 'typer>=0.7.0,<0.8.0']

setup_kwargs = {
    'name': 'private-reg',
    'version': '0.1.0',
    'description': 'A siple pytho program for managing container registry in private',
    'long_description': '# Private Registry\n\n\nThis is a simple python program to manage containers to upload, download and delete in private container regitry\n\n\n\nTo Install `private reg` use\n\n````\npip install private_reg\n````\n\nTo use in your py program:\n````\nfrom private_reg import container_reg\n````\n',
    'author': 'selva',
    'author_email': 'selva.g@subcom.tech',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)

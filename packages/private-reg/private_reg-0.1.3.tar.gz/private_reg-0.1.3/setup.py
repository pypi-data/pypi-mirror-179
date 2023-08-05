# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['private_reg']

package_data = \
{'': ['*']}

install_requires = \
['docker>=6.0.1,<7.0.0', 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['private_reg = '
                     'src.private_reg.container_registry:Private_registry']}

setup_kwargs = {
    'name': 'private-reg',
    'version': '0.1.3',
    'description': 'A simple pytho program for managing container registry in private',
    'long_description': '# Private Registry\n\n\nThis is a simple python program to manage containers to upload, download and delete in private container regitry\n\n\n\nTo Install `private reg` use\n\n````\npip install private_reg\n````\n\nTo use in your py program:\n\n````\nfrom private_reg import container_registry\n````\n\ncreate an object with class `Private_registry` in `container_registry` \nexample:\n````\nx = container_registry.Private_registry()\n````\n\n\n\n\n\n\nlist of functions in container_registry.Private_registry\n\n`is_container_running()` return status true or false whether a container is running with given name or not\n\n`check_repo_in_pvt_reg()` prints the repos in private registry\n\n`setup_pvt_registry()` starts private registry with a given conatiner name as class object\n\n`pull_image()` Pulls image from docker hub if --no-private-reg or pulls image from private-container-registry by default\n\n`push_image()` Push image to private_container_registry \n\n`delete_image()` Deletes image from private_containe_registry by default \n\n',
    'author': 'selva',
    'author_email': 'selva.g@subcom.tech',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)

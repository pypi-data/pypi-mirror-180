# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['my_tools']

package_data = \
{'': ['*'], 'my_tools': ['dist/*']}

install_requires = \
['einops>=0.4.1,<0.5.0',
 'numba>=0.56.2,<0.57.0',
 'numpy>=1.22,<2.0',
 'pandas>=1.4.0,<2.0.0',
 'pytest>=7.1.3,<8.0.0',
 'pytorch-lightning>=1.6,<2.0',
 'scikit-learn>=1.2.0,<2.0.0',
 'scipy>=1.7,<2.0',
 'torch>=1.12.1,<2.0.0',
 'transformers>=4.16,<5.0',
 'trash-cli>=0.22,<0.23',
 'wandb>=0.13.3,<0.14.0']

setup_kwargs = {
    'name': 'dkoshman-my-tools',
    'version': '0.1.1',
    'description': '',
    'long_description': 'My tools.',
    'author': 'DimaKoshman',
    'author_email': 'koshmandk@yandex.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)

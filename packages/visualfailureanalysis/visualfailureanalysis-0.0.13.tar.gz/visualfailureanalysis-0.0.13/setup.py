# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['visualfailureanalysis']

package_data = \
{'': ['*']}

install_requires = \
['Flask>=2.2.2,<3.0.0',
 'Pillow>=9.3.0,<10.0.0',
 'PyPDF2>=2.11.2,<3.0.0',
 'albumentations>=1.3.0,<2.0.0',
 'dash>=2.7.0,<3.0.0',
 'matplotlib>=3.6.2,<4.0.0',
 'numpy>=1.23.5,<2.0.0',
 'pandas>=1.5.2,<2.0.0',
 'plotly>=5.11.0,<6.0.0',
 'scikit-learn>=1.1.3,<2.0.0',
 'scipy>=1.9.3,<2.0.0',
 'torchvision>=0.14.0,<0.15.0']

setup_kwargs = {
    'name': 'visualfailureanalysis',
    'version': '0.0.13',
    'description': 'Test Project',
    'long_description': '',
    'author': 'Levin Kobelke',
    'author_email': 'levin.kobelke@dkfz-heidelberg.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

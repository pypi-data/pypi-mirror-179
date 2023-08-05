# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kats',
 'kats.compat',
 'kats.data',
 'kats.detectors',
 'kats.detectors.meta_learning',
 'kats.metrics',
 'kats.models',
 'kats.models.ensemble',
 'kats.models.metalearner',
 'kats.models.nowcasting',
 'kats.models.reconciliation',
 'kats.tests',
 'kats.tests.compat',
 'kats.tests.data',
 'kats.tests.detectors',
 'kats.tests.detectors.meta_learning',
 'kats.tests.metrics',
 'kats.tests.models',
 'kats.tests.tsfeatures',
 'kats.tests.utils',
 'kats.tsfeatures',
 'kats.utils']

package_data = \
{'': ['*'], 'kats.tests': ['baseline/*'], 'kats.tests.models': ['baseline/*']}

install_requires = \
['matplotlib==3.6.0',
 'numba==0.56.3',
 'numpy==1.21.0',
 'pandas==1.3.5',
 'python-dateutil==2.8.0',
 'scikit-learn==1.1.2',
 'scipy==1.7.3',
 'seaborn==0.11.1',
 'statsmodels==0.12.2',
 'torch==1.12.1']

setup_kwargs = {
    'name': 'tinykats-corestack',
    'version': '0.2.0',
    'description': 'Stripped down version of Kats (facebookresearch/Kats)',
    'long_description': None,
    'author': 'Hem Chandra Padhalni',
    'author_email': 'hem.chandra@corestack.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)

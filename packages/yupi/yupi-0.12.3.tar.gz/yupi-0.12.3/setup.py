# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yupi',
 'yupi.core',
 'yupi.core.featurizers',
 'yupi.core.serializers',
 'yupi.generators',
 'yupi.graphics',
 'yupi.stats',
 'yupi.tracking',
 'yupi.transformations']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.2.0', 'nudged>=0.3.1', 'numpy>=1.16.5', 'opencv-python>=4.4.0']

setup_kwargs = {
    'name': 'yupi',
    'version': '0.12.3',
    'description': 'A package for tracking and analysing objects trajectories',
    'long_description': '<p align="center">\n<img src="logo.png" alt="Logo"><br>\n</p>\n\n<div align="center">\n<a href="https://www.python.org/downloads/release/python-370/"><img src="https://img.shields.io/badge/python-3.7-blue" alt="Python"></a>\n<a href="https://zenodo.org/badge/latestdoi/304602979"><img src="https://zenodo.org/badge/304602979.svg" alt="DOI"></a>\n<a href="https://pypi.org/project/yupi/"><img src="https://img.shields.io/pypi/v/yupi" alt="PyPI"></a>\n<a href="https://yupi.readthedocs.io/en/latest/"><img src="https://img.shields.io/readthedocs/yupi" alt="ReadTheDocs"></a>\n</div>\n\nStanding for *Yet Underused Path Instruments*, **yupi** is a set of tools designed\nfor collecting, generating and processing trajectory data.\n\n## **Main features**\n\n- **Convert raw data to trajectories** ... *different input manners*\n- **I/O operations with trajectories** ... *json and csv serializers*\n- **Trajectory extraction from video inputs** ... *even with moving camera*\n- **Artificial trajectory generation** ... *several models implemented*\n- **Trajectory basic operations** ... *rotation, shift, scaling, ...*\n- **Trajectory transformations** ... *filters, resamplers, ...*\n- **Statistical analysis rom trajectories ensembles** ... *turning angles histogram, velocity autocorrelation function, power spectral density, and much more ...*\n- **Results visualization** ... *each statistical observable has a related plot function*\n- **Spacial projection of trajectories** ... *for 2D and 3D trajectories*\n\n## Installation\n\nCurrent recommended installation method is via PyPI:\n\n```cmd\npip install yupi\n```\n\n## Compatibility\n\n- Python 3.7 or later\n- Ubuntu 18.04 or later\n- Windows 7 or later\n- macOS 10.12.6 (Sierra) or later.\n\n## Getting Started\n\nIn the [official documentation](https://yupi.readthedocs.io/en/latest/) there\nare some resources to start using the library: Tutorials, Examples  and a\ndetailed description of the API.\n\n## Examples\n\nCode examples (with additional multimedia resources) can be found in\n[this repository](https://github.com/yupidevs/yupi_examples). Additionally, in\nthe [Examples section](https://yupi.readthedocs.io/en/latest/examples/examples.html)\nof the documentation, you can find the same examples with additional comments\nand expected execution results in order to inspect the examples without actually\nexecuting them.\n',
    'author': 'Gustavo Viera-López',
    'author_email': 'gvieralopez@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/yupidevs/yupi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

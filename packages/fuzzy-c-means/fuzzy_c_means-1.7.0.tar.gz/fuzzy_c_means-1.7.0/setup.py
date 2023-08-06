# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fcmeans']

package_data = \
{'': ['*']}

install_requires = \
['joblib>=1.2.0,<2.0.0',
 'numpy>=1.21.1,<2.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'tabulate>=0.8.9,<0.9.0',
 'tqdm>=4.64.1,<5.0.0',
 'typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['fcm = fcmeans.cli:app']}

setup_kwargs = {
    'name': 'fuzzy-c-means',
    'version': '1.7.0',
    'description': 'A simple python implementation of Fuzzy C-means algorithm.',
    'long_description': '# fuzzy-c-means\n\n![GitHub](https://img.shields.io/github/license/omadson/fuzzy-c-means.svg)\n[![PyPI](https://img.shields.io/pypi/v/fuzzy-c-means.svg)](http://pypi.org/project/fuzzy-c-means/)\n[![Documentation Status](https://readthedocs.org/projects/fuzzy-c-means/badge/?version=latest)](https://fuzzy-c-means.readthedocs.io/en/latest/?badge=latest)\n[![GitHub last commit](https://img.shields.io/github/last-commit/omadson/fuzzy-c-means.svg)](https://github.com/omadson/fuzzy-c-means/commit/master)\n[![Downloads](https://pepy.tech/badge/fuzzy-c-means)](https://pepy.tech/project/fuzzy-c-means)\n[![DOI](https://zenodo.org/badge/186457481.svg)](https://zenodo.org/badge/latestdoi/186457481)\n\n\n**[Documentation](https://fuzzy-c-means.readthedocs.io/)** | **[Changelog](https://fuzzy-c-means.readthedocs.io/en/latest/CHANGELOG/)** | **[Citation](https://fuzzy-c-means.readthedocs.io/en/latest/citation/)**\n\n\n\n`fuzzy-c-means` is a Python module implementing the [Fuzzy C-means][1] clustering algorithm.\n\n## installation\nthe `fuzzy-c-means` package is available in [PyPI](https://pypi.org/project/fuzzy-c-means/). to install, simply type the following command:\n```\npip install fuzzy-c-means\n```\n## citation\nif you use `fuzzy-c-means` package in your paper, please cite it in your publication.\n```\n@software{dias2019fuzzy,\n  author       = {Madson Luiz Dantas Dias},\n  title        = {fuzzy-c-means: An implementation of Fuzzy $C$-means clustering algorithm.},\n  month        = may,\n  year         = 2019,\n  publisher    = {Zenodo},\n  doi          = {10.5281/zenodo.3066222},\n  url          = {https://git.io/fuzzy-c-means}\n}\n```\n\n<!-- ### citations\n - [Gene-Based Clustering Algorithms: Comparison Between Denclue, Fuzzy-C, and BIRCH](https://doi.org/10.1177/1177932220909851)\n - [Analisis Data Log IDS Snort dengan Algoritma Clustering Fuzzy C-Means](https://doi.org/10.24843/MITE.2020.v19i01.P14)\n - [Comparative Analysis between the k-means and Fuzzy c-means Algorithms to Detect UDP Flood DDoS Attack on a SDN/NFV Environment](https://doi.org/10.5220/0010176201050112)\n - [Mixture-of-Experts Variational Autoencoder for Clustering and Generating from Similarity-Based Representations on Single Cell Data](https://arxiv.org/abs/1910.07763)\n - [Fuzzy Clustering: an Application to Distributional Reinforcement Learning](https://doi.org/10.34726/hss.2021.86783)\n - [Fuzzy Clustering with Similarity Queries](https://arxiv.org/pdf/2106.02212.pdf)\n - [Robust Representation and Efficient Feature Selection Allows for Effective Clustering of SARS-CoV-2 Variants](https://arxiv.org/abs/2110.09622)\n - [Unsupervised clustering-based spectral analysis of bio-dyed textile samples](http://urn.fi/urn:nbn:fi:uef-20211291) -->\n\n\n## contributing and support\n\nthis project is open for contributions. here are some of the ways for you to contribute:\n - bug reports/fix\n - features requests\n - use-case demonstrations\n\nplease open an [issue](https://github.com/omadson/fuzzy-c-means/issues) with enough information for us to reproduce your problem. A [minimal, reproducible example](https://stackoverflow.com/help/minimal-reproducible-example) would be very helpful.\n\nto make a contribution, just fork this repository, push the changes in your fork, open up an issue, and make a pull request!\n\n<!-- ## contributors\n - [Madson Dias](https://github.com/omadson)\n - [Dirk Nachbar](https://github.com/dirknbr)\n - [Alberth Florêncio](https://github.com/zealberth) -->\n\n[1]: https://doi.org/10.1016/0098-3004(84)90020-7\n[2]: http://scikit-learn.org/\n',
    'author': 'Madson Dias',
    'author_email': 'madsonddias@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/omadson/fuzzy-c-means',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

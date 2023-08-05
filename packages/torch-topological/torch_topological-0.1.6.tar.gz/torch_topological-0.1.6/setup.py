# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['torch_topological',
 'torch_topological.data',
 'torch_topological.datasets',
 'torch_topological.examples',
 'torch_topological.nn',
 'torch_topological.utils']

package_data = \
{'': ['*']}

install_requires = \
['POT>=0.8.0,<0.9.0',
 'giotto-ph>=0.2.0,<0.3.0',
 'gudhi>=3.4.1,<4.0.0',
 'matplotlib>=3.5.0,<4.0.0',
 'torch>=1.10.1,<2.0.0']

setup_kwargs = {
    'name': 'torch-topological',
    'version': '0.1.6',
    'description': 'A framework for topological machine learning based on `pytorch`.',
    'long_description': '<img src="https://raw.githubusercontent.com/aidos-lab/pytorch-topological/main/torch_topological.svg" height=128 alt="`pytorch-topological` icon" />\n\n# `pytorch-topological`: A topological machine learning framework for `pytorch`\n\n[![Documentation](https://readthedocs.org/projects/pytorch-topological/badge/?version=latest)](https://pytorch-topological.readthedocs.io/en/latest/?badge=latest) [![Maintainability](https://api.codeclimate.com/v1/badges/397f53d1968f01b86e74/maintainability)](https://codeclimate.com/github/aidos-lab/pytorch-topological/maintainability) ![GitHub contributors](https://img.shields.io/github/contributors/aidos-lab/pytorch-topological) ![PyPI - License](https://img.shields.io/pypi/l/torch_topological) ![PyPI](https://img.shields.io/pypi/v/torch_topological) [![Tests](https://github.com/aidos-lab/pytorch-topological/actions/workflows/run_tests.yaml/badge.svg)](https://github.com/aidos-lab/pytorch-topological/actions/workflows/run_tests.yaml)\n\n`pytorch-topological` (or `torch_topological`) is a topological machine\nlearning framework for [PyTorch](https://pytorch.org). It aims to\ncollect *loss terms* and *neural network layers* in order to simplify\nbuilding the next generation of topology-based machine learning tools.\n\n# Topological machine learning in a nutshell \n\n*Topological machine learning* refers to a new class of machine learning\nalgorithms that are able to make use of topological features in data\nsets. In contrast to methods based on a purely geometrical point of\nview, topological features are capable of focusing on *connectivity\naspects* of a data set. This provides an interesting fresh perspective\nthat can be used to create powerful hybrid algorithms, capable of\nyielding more insights into data.\n\nThis is an *emerging research field*, firmly rooted in computational\ntopology and topological data analysis. If you want to learn more about\nhow topology and geometry can work in tandem, here are a few resources\nto get you started:\n\n- Amézquita et al., [*The Shape of Things to Come: Topological Data Analysis and Biology,\n  from Molecules to Organisms*](https://doi.org/10.1002/dvdy.175), Developmental Dynamics\n  Volume 249, Issue 7, pp. 816--833, 2020.\n\n- Hensel et al., [*A Survey of Topological Machine Learning Methods*](https://www.frontiersin.org/articles/10.3389/frai.2021.681108/full),\n  Frontiers in Artificial Intelligence, 2021.\n\n# Installation and requirements\n\n`torch_topological` requires Python 3.9. More recent versions might work\nbut necessitate building some dependencies by yourself; Python 3.9\ncurrently offers the smoothest experience.\nIt is recommended to use the excellent [`poetry`](https://python-poetry.org) framework\nto install `torch_topological`:\n\n```\npoetry add torch-topological\n```\n\nAlternatively, use `pip` to install the package:\n\n```\npip install -U torch-topological\n```\n\n# Usage\n\n`torch_topological` is still a work in progress. You can [browse the documentation](https://pytorch-topological.readthedocs.io)\nor, if code reading is more your thing, dive directly into [some example\ncode](./torch_topological/examples).\n\nHere is a list of *other* projects that are using `torch_topological`:\n\n- [SHAPR](https://github.com/marrlab/SHAPR_torch), a method for for\n  predicting the 3D cell shape of individual cells based on 2D\n  microscopy images\n\nThis list is incomplete---you can help expanding it by using\n`torch_topological` in your own projects! :innocent:\n\n# Contributing\n\nCheck out the [contribution guidelines](CONTRIBUTING.md) or the [road\nmap](ROADMAP.md) of the project.\n\n# Acknowledgements\n\nOur software and research does not exist in a vacuum. `pytorch-topological` is standing\non the shoulders of proverbial giants. In particular, we want to thank the\nfollowing projects for constituting the technical backbone of the\nproject:\n\n| [`giotto-tda`](https://github.com/giotto-ai/giotto-tda)       | [`gudhi`](https://github.com/GUDHI/gudhi-devel)<br />       |\n|---------------------------------------------------------------|-------------------------------------------------------------|\n| <img src="logos/giotto.jpg" height=128 alt="`giotto` icon" /> | <img src="logos/gudhi.png" height=128 alt="`GUDHI` icon" /> |\n\nFurthermore, `pytorch-topological` draws inspiration from several\nprojects that provide a glimpse into the wonderful world of topological\nmachine learning:\n\n- [`difftda`](https://github.com/MathieuCarriere/difftda) by [Mathieu Carrière](https://github.com/MathieuCarriere)\n\n- [`Ripser`](https://github.com/Ripser/ripser) by [Ulrich Bauer](https://github.com/ubauer)\n\n- [`Teaspoon`](https://lizliz.github.io/teaspoon/) by [Elizabeth Munch](https://elizabethmunch.com/) and her team\n\n- [`TopologyLayer`](https://github.com/bruel-gabrielsson/TopologyLayer) by [Rickard Brüel Gabrielsson](https://github.com/bruel-gabrielsson)\n\n- [`topological-autoencoders`](https://github.com/BorgwardtLab/topological-autoencoders) by [Michael Moor](https://github.com/mi92), [Max Horn](https://github.com/ExpectationMax), and [Bastian Rieck](https://github.com/Pseudomanifold)\n\n- [`torchph`](https://github.com/c-hofer/torchph) by [Christoph Hofer](https://github.com/c-hofer) and [Roland Kwitt](https://github.com/rkwitt)\n\nFinally, `pytorch-topological` makes heavy use of [`POT`](https://pythonot.github.io), the Python Optimal Transport Library.\nWe are indebted to the many contributors of all these projects.\n',
    'author': 'Bastian Rieck',
    'author_email': 'bastian@rieck.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9',
}


setup(**setup_kwargs)

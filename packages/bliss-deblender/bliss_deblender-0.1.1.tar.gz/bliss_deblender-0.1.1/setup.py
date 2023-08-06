# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bliss', 'bliss.datasets', 'bliss.models', 'bliss.models.vae']

package_data = \
{'': ['*']}

install_requires = \
['astropy>=4.2.1',
 'einops>=0.3.0',
 'galsim>=2.2.4',
 'hydra-core>=1.0.4',
 'matplotlib>=3.3.3',
 'nflows>=0.14',
 'numpy>=1.18.5',
 'pytorch-lightning>=1.5.1',
 'scikit-learn>=0.24.2',
 'scipy>=1.4.1',
 'seaborn>=0.11.2',
 'torch>=1.9',
 'torchmetrics>=0.5.1']

setup_kwargs = {
    'name': 'bliss-deblender',
    'version': '0.1.1',
    'description': 'Bayesian Light Source Separator',
    'long_description': "![](http://portal.nersc.gov/project/dasrepo/celeste/sample_sky.jpg)\n\n\nBayesian Light Source Separator (BLISS)\n========================================\n[![](https://img.shields.io/badge/docs-master-blue.svg)](https://prob-ml.github.io/bliss/)\n![tests](https://github.com/prob-ml/bliss/workflows/tests/badge.svg)\n[![codecov.io](https://codecov.io/gh/prob-ml/bliss/branch/master/graphs/badge.svg?branch=master&token=Jgzv0gn3rA)](http://codecov.io/github/prob-ml/bliss?branch=master)\n![case studies](https://github.com/prob-ml/bliss/actions/workflows/case_studies.yml/badge.svg)\n\n# Introduction\n\nBLISS is a Bayesian method for deblending and cataloging light sources. BLISS provides\n  - __Accurate estimation__ of parameters in blended field.\n  - __Calibrated uncertainties__ through fitting an approximate Bayesian posterior.\n  - __Scalability__ of Bayesian inference to entire astronomical surveys.\n\nBLISS uses state-of-the-art variational inference techniques including\n  - __Amortized inference__, in which a neural network maps telescope images to an approximate Bayesian posterior on parameters of interest.\n  - __Variational auto-encoders__ (VAEs) to fit a flexible model for galaxy morphology and deblend galaxies.\n  - __Wake-sleep algorithm__ to jointly fit the approximate posterior and model parameters such as the PSF and the galaxy VAE.\n\n# Installation\n\nBLISS is pip installable with the following command: \n\n```bash\npip install bliss-deblender\n``` \n\nand the required dependencies are listed in the ``[tool.poetry.dependencies]`` block of the ``pyproject.toml`` file.\n\n# Installation (Developers)\n\n1. To use and install `bliss` you first need to install [poetry](https://python-poetry.org/docs/).\n\n2. Then, install the [fftw](http://www.fftw.org) library (which is used by `galsim`). With Ubuntu you can install it by running\n\n```bash\nsudo apt-get install libfftw3-dev\n```\n\n3. Install git-lfs if you haven't already installed it for another project:\n\n```bash\ngit-lfs install\n```\n\n4. Now download the bliss repo and fetch some pre-trained models and test data from git-lfs:\n\n```bash\ngit clone https://github.com/prob-ml/bliss.git\n```\n\n5. To create a poetry environment with the `bliss` dependencies satisified, run\n\n```bash\ncd bliss\npoetry install\npoetry shell\n```\n\n6. Verify that bliss is installed correctly by running the tests both on your CPU (default) and on your GPU:\n\n```bash\npytest\npytest --gpu\n```\n\n7. Finally, if you are planning to contribute code to this repository, consider installing our pre-commit hooks so that your code commits will be checked locally for compliance with our coding conventions:\n\n```bash\npre-commit --install\n```\n\n# Latest updates\n## Galaxies\n   - BLISS now includes a galaxy model based on a VAE that was trained on Galsim galaxies.\n   - BLISS now includes an algorithm for detecting, measuring, and deblending galaxies.\n\n## Stars\n   - BLISS already includes the StarNet functionality from its predecessor repo: [DeblendingStarFields](https://github.com/Runjing-Liu120/DeblendingStarfields).\n\n\n# References\n\nMallory Wang, Ismael Mendoza, Cheng Wang, Camille Avestruz, and Jeffrey Regier. *Statistical Inference for Coadded Astronomical Images.* Machine Learning and the Physical Sciences workshop, NeurIPS 2022. [arXiv:2211.09300](https://arxiv.org/abs/2211.09300)\n\nDerek Hansen, Ismael Mendoza, Runjing Liu, Ziteng Pang, Zhe Zhao, Camille Avestruz, and Jeffrey Regier. *Scalable Bayesian Inference for Detection and Deblending in Astronomical Images*. ICML Workshop on Machine Learning for Astrophysics, 2022. [arXiv:2207.05642](https://arxiv.org/abs/2207.05642)\n\nRunjing Liu, Jon D. McAuliffe, Jeffrey Regier, and The LSST Dark Energy Science Collaboration. *Variational Inference for Deblending Crowded Starfields*, 2021. [arXiv:2102.02409](https://arxiv.org/abs/2102.02409)\n",
    'author': 'Ismael Mendoza',
    'author_email': 'imendoza@umich.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/prob-ml/bliss',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['mealsearchpy']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.5.2,<2.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'mealsearchpy',
    'version': '0.1.1',
    'description': 'A Python package for people to find their favourite recipes.',
    'long_description': '# mealsearchpy\n\nA Python package for people to find their favourite recipes.\n\n## Installation\n\n```bash\n$ pip install mealsearchpy\n```\n\n## Usage\n\n- TODO\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`mealsearchpy` was created by Anni Dai. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`mealsearchpy` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'Anni Dai',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/QMSS-G5072-2022/Dai_Anni/tree/main/Final_Project/mealsearchpy',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

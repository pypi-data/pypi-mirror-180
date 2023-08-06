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
    'version': '0.1.2',
    'description': 'A Python package for people to find their favourite recipes.',
    'long_description': '# mealsearchpy\n\nA Python package for people to search what they still have left in the fridge and provide relevent recipes the food gets wasted by using Recipe Search API. The package comprises the functionality of allowing users to enter the left ingridients left in the fridge, such as "chicken", "potato" as input and return relevent recipes, which inlcudes 5 functions:\n1) search_meal(food_item, num_recipes): Show the recipes based on the food item(s) entered and the number of recipes user wants to generate.\n2) health_meal(food_item, health_type, calories, num_recipes): Show the recipes based on the food item(s), health type(s), calories entered and the number of recipes user wants to generate.\n3) diet_meal(food_item, diet_type, calories, num_recipes): Show the recipes based on the food item(s), diet type(s), calories entered and the number of recipes user wants to generate.\n4) quick_meal(food_item, time, num_recipes): Show the recipes based on the food item(s), and cook time entered and the number of recipes user wants to generate.\n5) cuisine_meal(food_item, cuisine_type, num_recipes): Show the recipes based on the food item(s), cuisine type(s) entered and the number of recipes user wants to generate.\n\n* API: Recipe Search API\n* Home Page: https://api.edamam.com\n* API Portal: https://api.edamam.com/api/recipes/v2\n* Authenticaiton: This API need users to REGISTER to get the API ID and API key for authentication in order to explore the recipes data. \n\n## Installation\n\n```bash\n$ pip install mealsearchpy\n```\nThe package has been published to pypi.\n* pypi:https://pypi.org/project/mealsearchpy/\n## Usage\n\n- TODO\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`mealsearchpy` was created by Anni Dai. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`mealsearchpy` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
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

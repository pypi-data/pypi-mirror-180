# mealsearchpy

A Python package for people to search what they still have left in the fridge and provide relevent recipes the food gets wasted by using Recipe Search API. The package comprises the functionality of allowing users to enter the left ingridients left in the fridge, such as "chicken", "potato" as input and return relevent recipes, which inlcudes 5 functions:
1) search_meal(food_item, num_recipes): Show the recipes based on the food item(s) entered and the number of recipes user wants to generate.
2) health_meal(food_item, health_type, calories, num_recipes): Show the recipes based on the food item(s), health type(s), calories entered and the number of recipes user wants to generate.
3) diet_meal(food_item, diet_type, calories, num_recipes): Show the recipes based on the food item(s), diet type(s), calories entered and the number of recipes user wants to generate.
4) quick_meal(food_item, time, num_recipes): Show the recipes based on the food item(s), and cook time entered and the number of recipes user wants to generate.
5) cuisine_meal(food_item, cuisine_type, num_recipes): Show the recipes based on the food item(s), cuisine type(s) entered and the number of recipes user wants to generate.

* API: Recipe Search API
* Home Page: https://api.edamam.com
* API Portal: https://api.edamam.com/api/recipes/v2
* Authenticaiton: This API need users to REGISTER to get the API ID and API key for authentication in order to explore the recipes data. 

## Installation

```bash
$ pip install mealsearchpy
```
The package has been published to pypi.
* pypi:https://pypi.org/project/mealsearchpy/
## Usage

- TODO

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`mealsearchpy` was created by Anni Dai. It is licensed under the terms of the MIT license.

## Credits

`mealsearchpy` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

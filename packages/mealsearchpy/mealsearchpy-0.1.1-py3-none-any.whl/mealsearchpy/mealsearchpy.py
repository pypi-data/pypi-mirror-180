import requests
import json
import pandas as pd

def read_api(params):
    """
    Get the data from API

    Parameters
    ----------
    params: dict
        Contains the keyword of the query, includes app_id, app_key and others

    Returns
    ----------
    Return a dictionary that contains the data based on the query
    """
    url = 'https://api.edamam.com/api/recipes/v2'
    r = requests.get(url, params=params)
    dic = r.json()
    return dic

def search(dic, criteria, num_recipes, food_item):
    """
    Perform search based on the criteria

    Parameters
    ----------
    dic: dict
        Contains the data based on the query
    criteria: list
        Contains the criteria that wants to show users.
    num_recipes: int
        Number of recipes that user want to see
    food_item: str
        Food items that users want to have in the recipe, must be separated by ","
        
    Returns
    ----------
    Return a dictionary that contains the data with these criteria, based on the query
    """
    data = {}
    max_num_recipes = len(dic['hits'])
    if num_recipes > max_num_recipes:
        raise Exception("Number of recipes entered exceed the search maximum " + str(
            max_num_recipes) + ', please try a number lower than this')

    i = 0
    num_search = 0
    while i < num_recipes and num_search < max_num_recipes:
        R = []
        for l in criteria:
            temp = dic['hits'][num_search]['recipe'][l]
            if l == 'totalTime':
                if temp == float(0):
                    temp = 'NA'
            if l == "label":
                label_flag = True
                for item in food_item.split(","):
                    if item.lower() not in temp.lower():
                        label_flag = False

            R.append(temp)
        num_search += 1

        if not label_flag:
            continue

        i += 1
        data['recipe' + str(i)] = R
    return data
        

class recipe:
    """
    A class to represent recipes.

    ...

    Attributes
    ----------
    app_id : str
        API id for requesting the API
    app_key : str
        API key for requesting the API
    typ : str
        Type of the request

    Methods
    -------
    search_meal(food_item, num_recipes):
        Show the recipes based on the food item(s) entered and the number of recipes user wants to generate.
    health_meal(food_item, health_type, calories, num_recipes):
        Show the recipes based on the food item(s), health type(s), calories entered and the number of recipes user wants to generate.
    diet_meal(food_item, diet_type, calories, num_recipes):
        Show the recipes based on the food item(s), diet type(s), calories entered and the number of recipes user wants to generate.
    quick_meal(food_item, time, num_recipes):
        Show the recipes based on the food item(s), and cook time entered and the number of recipes user wants to generate.
    cuisine_meal(food_item, cuisine_type, num_recipes):
        Show the recipes based on the food item(s), cuisine type(s) entered and the number of recipes user wants to generate.
    """

    def __init__(self, app_id, app_key, typ = 'public'):
        """
        Constructs all the necessary attributes for the recipe object.

        Parameters
        ----------
        app_id : str
            API id for requesting the API
        app_key : str
            API key for requesting the API
        typ : str
            Type of the request
        """

        self.app_id = app_id
        self.app_key = app_key
        self.typ = typ


    #Function1:
    def search_meal(self, food_item, num_recipes):
        """
        Show the recipes based on the food item(s) entered and the number of recipes user wants to generate.

        Parameters
        ----------
        food_item : str
            Key word(s) users want to search for recipes, seperated by ','
            eg. food_item = 'beef'; food_item = 'chicken, onion'
        num_recipes : int
            Number of recipes user wants to generate

        Returns
        -------
        Return a dataframe of recipes which contains the parameters of recipe name, instruction url, health labels, diet labels, ingredients, total cook time, and cuisine type.

        Examples
        --------
        >>> from mealsearchpy import mealsearchpy
        >>> my_recipe = mealsearchpy.recipe("cacd8be3","38390bbee98a285ca4d3a68cde6a0e0a")
        >>> food_item = 'pork, potato'
        >>> num_recipes = 1
        >>> my_recipe.search_meal(food_item, num_recipes)
        	            recipe1
        label	        Pork Potato Soup
        url	            http://www.bbcgoodfood.com/recipes/8927/
        healthLabels    [Dairy-Free, Gluten-Free, Wheat-Free, Egg-Free, Peanut-Free, Tree-Nut-Free, Soy-Free, Fish-Free, Shellfish-Free, Pork-Free, Crustacean-Free, Celery-Free, Mustard-Free, Sesame-Free, Lupine-Free, Mollusk-Free, Alcohol-Free, Sulfite-Free]
        dietLabels	    [High-Fiber, Low-Sodium]
        ingredientLines	[300 g of pork steak, 1 tbsp of olive oil, 1000 g of peeled quartered potatoes, 400 g of thinly shredded cabbage, 1 L of vegetable stock, 2 small chopped onions]
        totalTime	    NA
        cuisineType	    [french]
        """
        params = {"app_id": self.app_id, "app_key": self.app_key, "type": self.typ}
        params['q'] = food_item
        dic = read_api(params)
        criteria = ['label', 'url', 'healthLabels', 'dietLabels', 'ingredientLines', 'totalTime', 'cuisineType']

        data = search(dic, criteria, num_recipes, food_item)
        if len(data) == 0:
            print("There is no recipe that match your query, please try other keywords")
        
        df = pd.DataFrame(data, index = criteria)
        return df

    #Function2:
    def health_meal(self, food_item, health_type, calories, num_recipes):
        """
        Show the recipes based on the food item(s), health type(s), calories entered and the number of recipes user wants to generate.

        Parameters
        ----------
        food_item : str
            Key word(s) users want to search for recipes, seperated by ','
            eg. food_item = 'beef'; food_item = 'chicken, onion'
        health_type : list of string
            The health type(s) users want to search for recipes which must be chosen from alcohol-cocktail, alcohol-free, celery-free, crustacean-free, dairy-free, DASH, egg-free, fish-free, fodmap-free, gluten-free, immuno-supportive, keto-friendly, kidney-friendly, kosher, low-potassium, low-sugar, lupine-free, Mediterranean, mollusk-free, mustard-free,No-oil-added, paleo, peanut-free, pecatarian, pork-free, red-meat-free, sesame-free, shellfish-free, soy-free, sugar-conscious, sulfite-free, tree-nut-free, vegan, vegetarian, wheat-free.
            eg. health_type = ['egg-free']; health_type = ['egg-free', 'fish-free']
        calories : str
            Calories range users want to search for recipes which can be in the forms of MIN+, MIN-MAX, MAX
            eg. calories = '100+'; calories = '100-300'; calories = '300'
        num_recipes : int
            Number of recipes user wants to generate

        Returns
        -------
        Return a dataframe of recipes which contains the parameters of recipe name, instruction url, health labels, ingredients, total cook time, and cuisine type.

        Examples
        --------
        >>> from mealsearchpy import mealsearchpy
        >>> my_recipe = mealsearchpy.recipe("cacd8be3","38390bbee98a285ca4d3a68cde6a0e0a")
        >>> food_item = 'pork, tomato'
        >>> health = ['egg-free', 'gluten-free', 'peanut-free']
        >>> calories = '100-300'
        >>> num_recipes = 1
        >>> my_recipe.health_meal(food_item, health, calories, num_recipes)
                        recipe1
        label	        Pork Tenderloin with Tomato-Peach Compote
        url	            https://www.epicurious.com/recipes/food/views/pork-tenderloin-with-tomato-peach-compote-354133
        healthLabels    [Keto-Friendly, Dairy-Free, Gluten-Free, Wheat-Free, Egg-Free, Peanut-Free, Tree-Nut-Free, Soy-Free, Fish-Free, Shellfish-Free, Crustacean-Free, Celery-Free, Mustard-Free, Sesame-Free, Lupine-Free, Mollusk-Free, Alcohol-Free]
        ingredientLines	[4 garlic cloves, 1 tablespoon chopped peeled ginger, 1 teaspoon curry powder, 2 (3/4-pound) pork tenderloins, 2 tablespoons vegetable oil, 1 medium onion, chopped, 3/4 pound tomatoes, cut into 1-inch pieces, 1 peach, chopped, 2 teaspoons chopped thyme, 1 teaspoon sugar (optional), Equipment: a mortar and pestle]
        totalTime	    NA
        cuisineType	    [british]
        """
        all_health_types = ['alcohol-cocktail', 'alcohol-free', 'celery-free', 'crustacean-free', 'dairy-free', 'DASH', 'egg-free', 'fish-free', 'fodmap-free', 'gluten-free', 'immuno-supportive', 'keto-friendly', 'kidney-friendly', 'kosher', 'low-potassium', 'low-sugar', 'lupine-free', 'Mediterranean', 'mollusk-free', 'mustard-free','No-oil-added', 'paleo', 'peanut-free', 'pecatarian', 'pork-free','red-meat-free', 'sesame-free', 'shellfish-free', 'soy-free', 'sugar-conscious', 'sulfite-free', 'tree-nut-free', 'vegan', 'vegetarian', 'wheat-free']
        if not all(item in all_health_types for item in health_type):
            raise Exception("The health type must be one of the followings: alcohol-cocktail, alcohol-free, celery-free, crustacean-free, dairy-free, DASH, egg-free, fish-free, fodmap-free, gluten-free, immuno-supportive, keto-friendly, kidney-friendly, kosher, low-potassium, low-sugar, lupine-free, Mediterranean, mollusk-free, mustard-free,No-oil-added, paleo, peanut-free, pecatarian, pork-free, red-meat-free, sesame-free, shellfish-free, soy-free, sugar-conscious, sulfite-free, tree-nut-free, vegan, vegetarian, wheat-free.")
    
        if "-" not in calories and '+' not in calories and not calories.isdigit():
            raise Exception("The format of calories must be min-max, min+ or max, eg 100-300, 100+, 300")
            
        params = {"app_id": self.app_id, "app_key": self.app_key, "type": self.typ}
        params['q'] = food_item
        params['health'] = health_type
        params['calories'] = calories
        dic = read_api(params)
        criteria = ['label', 'url', 'healthLabels', 'ingredientLines', 'totalTime', 'cuisineType']

        data = search(dic, criteria, num_recipes, food_item)
        if len(data) == 0:
            print("There is no recipe that match your query, please try other keywords")

        df = pd.DataFrame(data, index=criteria)
        return df
    
    
    #Function3:
    def diet_meal(self, food_item, diet_type, calories, num_recipes):
        """
        Show the recipes based on the food item(s), diet type(s), calories entered and the number of recipes user wants to generate.

        Parameters
        ----------
        food_item : str
            Key word(s) users want to search for recipes, seperated by ','
            eg. food_item = 'beef'; food_item = 'chicken, onion'
        diet_type : list of string
            The diet type(s) users want to search for recipes which must be chosen from balanced, high-fiber, high-protein, low-carb, low-fat, low-sodium.
            eg. diet_type = ['balanced']; health_type = ['balanced', 'low-carb']
        calories : str
            Calories range users want to search for recipes which can be in the forms of MIN+, MIN-MAX, MAX
            eg. calories = '100+'; calories = '100-300'; calories = '300'
        num_recipes : int
            Number of recipes user wants to generate

        Returns
        -------
        Return a dataframe of recipes which contains the parameters of recipe name, instruction url, diet labels, ingredients, total cook time, and cuisine type.

        Examples
        --------
        >>> from mealsearchpy import mealsearchpy
        >>> my_recipe = mealsearchpy.recipe("cacd8be3","38390bbee98a285ca4d3a68cde6a0e0a")
        >>> food_item = 'pork, potato'
        >>> diet = ['low-carb', 'low-sodium']
        >>> calories = '100-300'
        >>> num_recipes = 1
        >>> my_recipe.health_meal(food_item, diet, calories, num_recipes)
                        recipe1
        label	        Slow Cooker Pork with Sweet Potato and App
        url	            http://leanmeankitchen.com/slow-cooker-pork-with-sweet-potato-and-apple/
        dietLabels      [Low-Carb, Low-Sodium]
        ingredientLines	[* 2.5-3 lb pork loin, * 1 sweet potato, large, * 3 apple, * 1 tbsp onion powder, * 1 tbsp granulated garlic, * 1 tbsp ground black pepper, * 1/2 tbsp paprika, * 1/2 tsp sea salt, * 1 tbsp fresh rosemary, * 1 c filtered water]
        totalTime	    NA
        cuisineType	    [american]
        """
        all_diet_types = ['balanced', 'high-fiber', 'high-protein', 'low-carb', 'low-fat', 'low-sodium']
        if not all(item in all_diet_types for item in diet_type):
            raise Exception("The diet type must be one of the followings: balanced, high-fiber, high-protein, low-carb, low-fat, low-sodium.")
            
        if "-" not in calories and '+' not in calories and not calories.isdigit():
            raise Exception("The format of calories must be min-max, min+ or max, eg 100-300, 100+, 300")
    
        params = {"app_id": self.app_id, "app_key": self.app_key, "type": self.typ}
        params['q'] = food_item
        params['diet'] = diet_type
        params['calories'] = calories
        dic = read_api(params)
        criteria = ['label', 'url', 'dietLabels', 'ingredientLines', 'totalTime', 'cuisineType']
        
        data = search(dic, criteria, num_recipes, food_item)
        if len(data) == 0:
            print("There is no recipe that match your query, please try other keywords")

        df = pd.DataFrame(data, index=criteria)
        return df
    
    
    #Function4:
    def quick_meal(self, food_item, time, num_recipes):
        """
        Show the recipes based on the food item(s), and cook time entered and the number of recipes user wants to generate.

        Parameters
        ----------
        food_item : str
            Key word(s) users want to search for recipes, seperated by ','
            eg. food_item = 'beef'; food_item = 'chicken, onion'
        time : str
            time range users want to search for recipes which can be in the forms of MIN(min)+, MIN(min)-MAX(min), MAX(min)
            eg. time = '10+'; time = '10-60'; time = '60'
        num_recipes : int
            Number of recipes user wants to generate

        Returns
        -------
        Return a dataframe of recipes which contains the parameters of recipe name, instruction url, total cook time, ingredients, health labels, diet labels, and cuisine type.

        Examples
        --------
        >>> from mealsearchpy import mealsearchpy
        >>> my_recipe = mealsearchpy.recipe("cacd8be3","38390bbee98a285ca4d3a68cde6a0e0a")
        >>> food_item = 'chicken, tomato'
        >>> time = '10-60'
        >>> num_recipes = 1
        >>> my_recipe.health_meal(food_item, time, num_recipes)
                        recipe1
        label	        Chicken, Tomato and Bread Cubes with Lemon-Oregano Marinade
        url	            https://www.marthastewart.com/1003601/chicken-tomato-and-bread-cubes-lemon-oregano-marinade
        totalTime       50.0
        ingredientLines [1/2 cup olive oil, plus more for grill, 1/4 cup lemon juice (from 2 lemons), 3 tablespoons chopped fresh oregano, Salt and pepper, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1 1/2-inch pieces, 2 pints cherry tomatoes, 4 cups cubed crusty bread]
        healthLabels    [Sugar-Conscious, Mediterranean, DASH, Dairy-Free, Egg-Free, Peanut-Free, Tree-Nut-Free, Soy-Free, Fish-Free, Shellfish-Free, Pork-Free, Red-Meat-Free, Crustacean-Free, Celery-Free, Mustard-Free, Sesame-Free, Lupine-Free, Mollusk-Free, Alcohol-Free, Sulfite-Free, Kosher]
        dietLabels	    [Low-Carb]
        cuisineType	    [mediterranean]
        """
        params = {"app_id": self.app_id, "app_key": self.app_key, "type": self.typ}
        params['q'] = food_item
        params['time'] = time
        dic = read_api(params)
        criteria = ['label', 'url', 'totalTime', 'ingredientLines', 'healthLabels', 'dietLabels', 'cuisineType']

        data = search(dic, criteria, num_recipes, food_item)
        if len(data) == 0:
            print("There is no recipe that match your query, please try other keywords")

        df = pd.DataFrame(data, index=criteria)
        return df

    
    #Function5:
    def cuisine_meal(self, food_item, cuisine_type, num_recipes):
        """
        Show the recipes based on the food item(s), cuisine type(s) entered and the number of recipes user wants to generate.

        Parameters
        ----------
        food_item : str
            Key word(s) users want to search for recipes, seperated by ','
            eg. food_item = 'beef'; food_item = 'chicken, onion'
        cuisine_type : list of string
            The diet type(s) users want to search for recipes which must be chosen from american, asian, british, caribbean, central europe, chinese, eastern europe, french, greek, indian, italian, japanese, korean, kosher, mediterranean, mexican, middle eastern, nordic, south american, south east asian, world.
            eg. diet_type = ['american']
        num_recipes : int
            Number of recipes user wants to generate

        Returns
        -------
        Return a dataframe of recipes which contains the parameters of recipe name, instruction url, cuisine type, ingredients and total cook time.

        Examples
        --------
        >>> from mealsearchpy import mealsearchpy
        >>> my_recipe = mealsearchpy.recipe("cacd8be3","38390bbee98a285ca4d3a68cde6a0e0a")
        >>> food_item = 'chicken'
        >>> cuisine = ['chinese']
        >>> num_recipes = 1
        >>> my_recipe.health_meal(food_item, cuisine, num_recipes)
                        recipe1
        label	        Drunken Chicken Recipe
        url	            http://www.seriouseats.com/recipes/2012/07/drunken-chicken.html
        cuisineType     [chinese]
        ingredientLines	[2 whole chicken parts (two breasts, two leg/thighs, or a mix), totaling about 2 pounds, One 1-inch piece of ginger, Kosher salt, 1 cup Shaoxing rice wine, 1 cup chicken broth from simmering]
        totalTime	    1440.0
        """
        all_cuisine_types = ['american', 'asian', 'british', 'caribbean', 'central europe', 'chinese', 'eastern europe', 'french', 'greek', 'indian', 'italian', 'japanese','korean', 'kosher', 'mediterranean', 'mexican', 'middle eastern', 'nordic', 'south american', 'south east asian','world']
        
        if not all(item in all_cuisine_types for item in cuisine_type):
            raise Exception("The cuisine type must be one of the followings: american, asian, british, caribbean, central europe, chinese, eastern europe, french, greek, indian, italian, japanese, korean, kosher, mediterranean, mexican, middle eastern, nordic, south american, south east asian, world.")
            
        params = {"app_id": self.app_id, "app_key": self.app_key, "type": self.typ}
        params['q'] = food_item
        params['cuisineType'] = cuisine_type
        dic = read_api(params)
        criteria = ['label', 'url', 'cuisineType', 'ingredientLines', 'totalTime']

        data = search(dic, criteria, num_recipes, food_item)
        if len(data) == 0:
            print("There is no recipe that match your query, please try other keywords")

        df = pd.DataFrame(data, index=criteria)
        return df

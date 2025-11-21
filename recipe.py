import requests
def find_recipe(ingredients, api_key):
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    # Parameters to send to API
    params = {
        "ingredients": ingredients, 
        "number": 10,                 # number of recipes to return
        "apiKey": api_key
    }
    # Send request to Spoonacular API
    response = requests.get(url, params=params)
    # If request failed
    if response.status_code != 200:
        print("Something went wrong!")
        return
    # Convert to JSON
    recipes = response.json()
    print("\n Recipes you can try:")
    for recipe in recipes:
        print(f"- {recipe['title']}")
if __name__ == "__main__":
    print(" Ingredients to Recipe Finder")
    user_ingredients = input("Enter ingredients: ")
    api_key = "3f4220e7eb524161bf91d4ed36a965a6"  
    find_recipe(user_ingredients, api_key)

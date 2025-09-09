# Example: Using TypedDict Recipe class

from typing import TypedDict, List

class Recipe(TypedDict):
    ingredients: List[str]    # List of ingredient names
    cooking_time: int         # Time in minutes
    difficulty: str          # "Easy", "Medium", "Hard"
    servings: int            # Number of servings

# === CREATING RECIPES ===
print("=== CREATING RECIPES ===")

# Method 1: Create dictionary directly (most common)
pasta_recipe = {
    "ingredients": ["pasta", "tomato sauce", "cheese", "garlic"],
    "cooking_time": 20,
    "difficulty": "Easy",
    "servings": 4
}

# Method 2: Start empty and add items
pizza_recipe = {}
pizza_recipe["ingredients"] = ["dough", "cheese", "pepperoni", "tomato sauce"]
pizza_recipe["cooking_time"] = 30
pizza_recipe["difficulty"] = "Medium"
pizza_recipe["servings"] = 6

print("Pasta recipe:", pasta_recipe)
print("Pizza recipe:", pizza_recipe)

# === USING THE RECIPES ===
print("\n=== USING THE RECIPES ===")

def cook_recipe(recipe: Recipe):
    """Function that takes a Recipe TypedDict"""
    print(f"Cooking {recipe['difficulty']} recipe...")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"Time needed: {recipe['cooking_time']} minutes")
    print(f"Serves: {recipe['servings']} people")
    print("---")

# Call the function with our recipes
cook_recipe(pasta_recipe)
cook_recipe(pizza_recipe)

# === TYPE SAFETY BENEFITS ===
print("=== TYPE SAFETY BENEFITS ===")

# This would work (correct types)
good_recipe = {
    "ingredients": ["flour", "eggs", "milk"],
    "cooking_time": 15,
    "difficulty": "Easy",
    "servings": 2
}

# This would cause type errors (if using a type checker like mypy):
# bad_recipe = {
#     "ingredients": "just flour",  # Should be List[str], not str
#     "cooking_time": "twenty",     # Should be int, not str
#     "difficulty": "Easy",
#     "servings": 2
# }

print("Good recipe:", good_recipe)
cook_recipe(good_recipe)

# === WORKING WITH MULTIPLE RECIPES ===
print("=== WORKING WITH MULTIPLE RECIPES ===")

all_recipes = [pasta_recipe, pizza_recipe, good_recipe]

def find_quick_recipes(recipes: List[Recipe], max_time: int):
    """Find recipes that take less than max_time minutes"""
    quick_recipes = []
    for recipe in recipes:
        if recipe["cooking_time"] <= max_time:
            quick_recipes.append(recipe)
    return quick_recipes

quick_recipes = find_quick_recipes(all_recipes, 25)
print(f"Recipes under 25 minutes: {len(quick_recipes)}")
for recipe in quick_recipes:
    print(f"- {recipe['difficulty']} recipe ({recipe['cooking_time']} min)")

# === MODIFYING RECIPES ===
print("\n=== MODIFYING RECIPES ===")

def double_recipe(recipe: Recipe) -> Recipe:
    """Double the servings and adjust ingredients"""
    new_recipe = recipe.copy()  # Create a copy
    new_recipe["servings"] = recipe["servings"] * 2
    new_recipe["cooking_time"] = recipe["cooking_time"] + 5  # Add 5 min for larger batch
    return new_recipe

doubled_pasta = double_recipe(pasta_recipe)
print("Original pasta:", pasta_recipe["servings"], "servings")
print("Doubled pasta:", doubled_pasta["servings"], "servings")
print("Doubled pasta time:", doubled_pasta["cooking_time"], "minutes")

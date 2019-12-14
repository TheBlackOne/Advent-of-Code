import math

class IngridientsCalculator:
    def __init__(self, _input):
        self.leftover = {}
        self.crafting_table = {}
        self.start_product = ""
        self.parse_input(_input)

    def parse_input(self, _input):
        for line in _input.split('\n'):
            ingredients, product = line.split(" => ")
            quantity, product = product.split(" ")
            ingredient_list = [int(quantity)]

            for ingredient in ingredients.split(", "):
                quantity, ingredient = ingredient.split(" ")
                ingredient_list.append((ingredient, int(quantity)))

            self.crafting_table[product] = ingredient_list

    def set_start_product(self, product, quantity, ingridient, ingridient_quantity):
        self.crafting_table[product] = [quantity, (ingridient, ingridient_quantity)]
        self.start_product = product

    def minimize(self, ingredients):
        min_list = {}
        for ingredient in ingredients:
            ingredient, quantity = ingredient
            if ingredient not in min_list.keys():
                min_list[ingredient] = 0
            min_list[ingredient] += quantity

        result = []
        for ingredient, quantity in min_list.items():
            result.append((ingredient, quantity))

        return result

    def get_ingredients(self, product, quantity):
        result = []

        if product == "ORE":
            result.append((product, quantity))
        else:
            ingredients = self.crafting_table[product]
            product_quantity = ingredients[0]
            
            if product in self.leftover.keys():
                if self.leftover[product] > quantity:
                    self.leftover[product] -= quantity
                    quantity = 0
                else:
                    quantity -= self.leftover[product]
                    self.leftover[product] = 0
                
            if quantity > 0:
                multiplier = math.ceil(quantity / product_quantity)
                num_leftover = (product_quantity * multiplier) - quantity
                if num_leftover > 0:
                    if product not in self.leftover.keys():
                        self.leftover[product] = 0
                    self.leftover[product] += num_leftover

                ingredients = ingredients[1:]
                for ingredient in ingredients:
                    ingredient, ingredient_quantity = ingredient
                    result.append((ingredient, ingredient_quantity * multiplier))

        return result

    def calculate_ore(self):
        num_ore = 0
        self.leftover = {}
        temp_ingredients = []

        start_product_quantity = self.crafting_table[self.start_product][0]
        ingredient_list = [(self.start_product, start_product_quantity)]

        while True:
            for ingredient in ingredient_list:
                ingredient, ingredient_quantity = ingredient
                temp_ingredients.extend(self.get_ingredients(ingredient, ingredient_quantity))
            temp_ingredients = self.minimize(temp_ingredients)

            if len(temp_ingredients) == 1 and temp_ingredients[0][0] == "ORE":
                num_ore = temp_ingredients[0][1]
                break
            else:
                ingredient_list = temp_ingredients
                temp_ingredients = []

        return num_ore
class Dish(object):
    def __init__(self, ingredients: list):
        self.ingredients = ingredients

    def __repr__(self):
        return f'dish({self.ingredients!r})'

    @classmethod
    def fish_and_chips(cls):
        return cls(['fish', 'potato'])

    @classmethod
    def spaghetti(cls):
        return cls(['noodles', 'tomato', 'orion', 'bacon'])


a = Dish.fish_and_chips()
print(a)
"""
dish(['fish', 'potato'])
"""
print(Dish.spaghetti())
"""
dish(['noodles', 'tomato', 'orion', 'bacon'])
"""

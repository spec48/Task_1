from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_available_buns_returns_list(self, database):
        buns = database.available_buns()
        assert isinstance(buns, list)

    def test_available_buns_returns_list_of_buns(self, database):
        buns = database.available_buns()
        for bun_in_list in buns:
            assert isinstance(bun_in_list, Bun)

    def test_available_buns_length_list_of_buns_is_3(self, database):
        buns = database.available_buns()
        assert len(buns) == 3

    def test_available_ingredients_returns_list(self, database):
        ingredients = database.available_ingredients()
        assert isinstance(ingredients, list)

    def test_available_ingredients_returns_list_of_ingredients(self, database):
        ingredients = database.available_ingredients()
        for ingredient_in_list in ingredients:
            assert isinstance(ingredient_in_list, Ingredient)

    def test_available_ingredients_length_list_of_buns_is_6(self, database):
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6

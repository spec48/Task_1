from unittest.mock import Mock
import pytest
from data import THREE_INGREDIENTS, BUN_1
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def bun():
    return Bun(*BUN_1)

@pytest.fixture
def burger():
    burger = Burger()
    return burger

@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.name = 'Соус'
    ingredient.price = 80.0
    return ingredient

@pytest.fixture
def burger_with_ingredients(burger):
    for name, price in THREE_INGREDIENTS.items():
        ingredient = Mock()
        ingredient.name = name
        ingredient.price = price
        burger.add_ingredient(ingredient)
    return burger

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = BUN_1[0]
    bun.get_price.return_value = BUN_1[1]
    return bun

@pytest.fixture
def mock_ingredients():
    mock_ingredient_1 = Mock()
    mock_ingredient_1.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock_ingredient_1.get_name.return_value = "Соус"
    mock_ingredient_1.get_price.return_value = THREE_INGREDIENTS.get("Соус")
    mock_ingredient_2 = Mock()
    mock_ingredient_2.get_type.return_value = INGREDIENT_TYPE_FILLING
    mock_ingredient_2.get_name.return_value = "Котлета"
    mock_ingredient_2.get_price.return_value = THREE_INGREDIENTS.get("Котлета")
    return [mock_ingredient_1, mock_ingredient_2]

@pytest.fixture
def ingredient():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "Соус", THREE_INGREDIENTS.get("Соус"))

@pytest.fixture
def database():
    return Database()

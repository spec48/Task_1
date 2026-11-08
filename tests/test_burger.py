from unittest.mock import Mock
import pytest
from data import THREE_INGREDIENTS, EXPECTED_RECEIPT


class TestBurger:

    def test_set_buns_bun_is_set_success(self, bun, burger):
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_one_ingredient_success(self, mock_ingredient, burger):
        burger.add_ingredient(mock_ingredient)
        assert isinstance(burger.ingredients, list) and len(burger.ingredients) == 1


    @pytest.mark.parametrize("ingredient_to_remove, expected_list_length", [
        [0, 2],  # Удаление первого ингредиента
        [1, 2],  # Удаление второго ингредиента
        [2, 2]   # Удаление третьего ингредиента
    ]
                             )
    def test_remove_ingredient_success(self, mock_ingredient, burger_with_ingredients, ingredient_to_remove,
                                       expected_list_length):
        burger_with_ingredients.remove_ingredient(ingredient_to_remove)
        assert len(burger_with_ingredients.ingredients) == expected_list_length


    @pytest.mark.parametrize("ingredient_to_remove", [-4, 3])  # Удаление несуществующих ингредиентов
    def test_remove_invalid_ingredient_fail(self, mock_ingredient, burger_with_ingredients, ingredient_to_remove):
        with pytest.raises(IndexError):
            burger_with_ingredients.remove_ingredient(ingredient_to_remove)


    @pytest.mark.parametrize("ingredient_to_move, expected_ingredient_price", [
        [2, THREE_INGREDIENTS.get("Томаты, лук")],
        [1, THREE_INGREDIENTS.get("Котлета")],
        [0, THREE_INGREDIENTS.get("Соус")]
    ]
                             )
    def test_move_ingredient_move_to_start_success(self, burger_with_ingredients, ingredient_to_move,
                                              expected_ingredient_price):
        burger_with_ingredients.move_ingredient(ingredient_to_move, 0)
        assert burger_with_ingredients.ingredients[0].price == expected_ingredient_price


    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, result_price", [
            [100.0, [50.0, 30.0, 20.0], 300.0],  # С булкой и тремя ингредиентами
            [0.0, [50.0], 50.0],  # Без булки с одним ингредиентом
            [100.0, [], 200.0]  # С булкой без ингредиентов
        ]
    )
    def test_get_price_success(self, bun_price, ingredient_prices, result_price, burger):
        bun = Mock()
        bun.get_price.return_value = bun_price
        burger.bun = bun
        ingredients = []
        for price in ingredient_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            ingredients.append(ingredient)
        burger.ingredients = ingredients
        assert burger.get_price() == result_price


    def test_get_receipt_success(self, burger, mock_bun, mock_ingredients):
        burger.bun = mock_bun
        burger.ingredients = mock_ingredients
        assert burger.get_receipt() == EXPECTED_RECEIPT

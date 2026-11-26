import pytest
from data import BUN_1, BUN_2, BUN_3
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize("bun, price", [
        [BUN_1[0], 80.0],
        [BUN_2[0], 80.0],
        [BUN_3[0], 80.0]
    ]
                             )
    def test_get_name_returns_name(self, bun, price):
        any_bun = Bun(bun, price)
        assert any_bun.get_name() == bun


    @pytest.mark.parametrize("bun, price", [
        ["bun", BUN_1[1]],
        ["bun", BUN_2[1]],
        ["bun", BUN_3[1]]
    ]
                             )
    def test_get_price_returns_price(self, bun, price):
        any_bun = Bun(bun, price)
        assert any_bun.get_price() == price

import pytest

from unittest import mock

from software_testing.main import even_odd, sum_all, time_of_day, datetime, Product, Shop


# Unit tests for function even_odd
# ===================================================================
@pytest.mark.parametrize('test_arg,expected',
                         [(1, 'odd'),
                          (10, 'even'),
                          (-4, 'even'),
                          (1.0, 'odd')])
def test_even_odd(test_arg, expected):
    assert even_odd(test_arg) == expected


def test_even_odd_none_arg():
    test_arg = None

    with pytest.raises(TypeError):
        even_odd(test_arg)


# Unit tests for function sum_all
# ===================================================================
@pytest.mark.parametrize('test_arg,expected',
                         [((1, 2, 3), 6),
                          ((1.3, 4.9, 13.8), 20.0)])
def test_sum_all(test_arg, expected):
    assert sum_all(*test_arg) == expected


def test_sum_all_none_arg():
    test_arg = None

    with pytest.raises(TypeError):
        sum_all(test_arg)


# Unit tests for function datetime
# ===================================================================
@pytest.mark.parametrize('test_arg, expected',
                         [([2021, 5, 23, 8, 43, 21], 'morning'),
                          ([2021, 5, 23, 3, 12, 16], 'night'),
                          ([2021, 5, 23, 17, 50, 3], 'afternoon')])
@mock.patch('software_testing.main.datetime')
def test_time_of_day(mocked_datetime, test_arg, expected):
    mocked_datetime.now.return_value = datetime(*test_arg)
    assert time_of_day() == expected


# Testing Product's methods
# ===================================================================
@pytest.fixture
def meat():
    """Creates some product object for testing"""
    return Product('meat', 250, 10)


@pytest.fixture
def milk():
    """Creates some product object for testing"""
    return Product('milk', 35, 2)


def test_product_subtract_quantity(meat):
    meat.subtract_quantity(5)
    assert meat.quantity == 5


def test_product_add_quantity(meat):
    meat.add_quantity(5)
    assert meat.quantity == 15


def test_product_change_price(meat):
    meat.change_price(100)
    assert meat.price == 100


@pytest.fixture
def some_shop():
    """Returns some empty Shop object"""
    return Shop()


def test_shop_add_product(some_shop, milk, meat):
    assert some_shop.products == []
    some_shop.add_product(milk)
    assert some_shop.products == [milk]
    some_shop.add_product(meat)
    assert some_shop.products == [milk, meat]
    assert some_shop.products[1].price == 250
    assert some_shop.products[0].title == 'milk'


@pytest.fixture
def shop_meat_milk(milk, meat):
    """Returns Shop object with milk and meat"""
    return Shop([milk, meat])


def test_shop_get_product_index(shop_meat_milk):
    assert shop_meat_milk._get_product_index('milk') == 0
    assert shop_meat_milk._get_product_index('meat') == 1
    assert shop_meat_milk._get_product_index('hwrtysssert') is None
    with pytest.raises(TypeError):
        shop_meat_milk._get_product_index()


def test_shop_sell_product(shop_meat_milk):
    assert shop_meat_milk.money == 0
    assert shop_meat_milk.products[0].quantity == 2
    assert shop_meat_milk.sell_product('milk') == 35
    assert shop_meat_milk.products[0].quantity == 1
    assert shop_meat_milk.money == 35


def test_shop_sell_product_errors(shop_meat_milk):
    with pytest.raises(TypeError):
        shop_meat_milk.sell_product()
    with pytest.raises(ValueError):
        shop_meat_milk.sell_product('meat', 100)


def test_shop_sell_product_all(shop_meat_milk):
    shop_meat_milk.sell_product('meat', 10)
    assert shop_meat_milk._get_product_index('meat') is None
    assert shop_meat_milk.money == 2500

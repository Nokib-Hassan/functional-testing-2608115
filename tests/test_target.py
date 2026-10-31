import pytest

import target


@pytest.mark.parametrize(
    ("age", "expected"),
    [(0, False), (17, False), (18, True), (19, True), (100, True)],
)
def test_is_adult_boundaries(age, expected):
    assert target.is_adult(age) is expected


def test_is_adult_rejects_negative_age():
    with pytest.raises(ValueError, match="age cannot be negative"):
        target.is_adult(-1)


@pytest.mark.parametrize(
    ("celsius", "expected"),
    [(0, 32), (100, 212), (-40, -40), (12.345, 54.22), (0.1, 32.18)],
)
def test_celsius_to_fahrenheit(celsius, expected):
    result = target.celsius_to_fahrenheit(celsius)
    assert result == expected
    assert isinstance(result, (int, float))


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", 0),
        ("AEIOU", 5),
        ("Functional Testing", 6),
        ("rhythms", 0),
        ("aAa! 123", 3),
        ("über", 1),
    ],
)
def test_count_vowels(text, expected):
    assert target.count_vowels(text) == expected


def test_count_vowels_rejects_non_strings():
    with pytest.raises(TypeError, match="text must be a string"):
        target.count_vowels(None)


@pytest.mark.parametrize(("flag", "expected"), [(True, False), (False, True)])
def test_invert(flag, expected):
    assert target.invert(flag) is expected


@pytest.mark.parametrize("value", [0, 1, "true", None])
def test_invert_rejects_non_bool(value):
    with pytest.raises(TypeError, match="flag must be True or False"):
        target.invert(value)


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        (None, "Hello, Guest!"),
        ("", "Hello, Guest!"),
        ("   ", "Hello, Guest!"),
        ("Ada", "Hello, Ada!"),
        ("  Ada Lovelace  ", "Hello, Ada Lovelace!"),
    ],
)
def test_greet(name, expected):
    assert target.greet(name) == expected


def test_greet_non_string_follows_original_attribute_error():
    with pytest.raises(AttributeError):
        target.greet(42)


@pytest.mark.parametrize(
    ("numbers", "expected"),
    [([7], 7), ([1, 9, 3], 9), ([-5, -2, -8], -2), ([-1, 4, 2], 4), ([2.5, 2.5], 2.5)],
)
def test_find_max(numbers, expected):
    assert target.find_max(numbers) == expected


def test_find_max_empty_list():
    with pytest.raises(ValueError, match="list is empty"):
        target.find_max([])


@pytest.mark.parametrize(
    ("prices", "item", "expected"),
    [({"book": 10}, "book", 10), ({"book": "ten"}, "book", "ten"), ({}, "missing", None)],
)
def test_get_price(prices, item, expected):
    if expected is None:
        with pytest.raises(KeyError, match="missing not found"):
            target.get_price(prices, item)
    else:
        assert target.get_price(prices, item) == expected


@pytest.mark.parametrize(
    ("pair", "expected"),
    [([1, 2], (2, 1)), ((1, "two"), ("two", 1)), ("ab", ("b", "a"))],
)
def test_swap(pair, expected):
    result = target.swap(pair)
    assert result == expected
    assert isinstance(result, tuple)


@pytest.mark.parametrize("pair", [(), (1,), (1, 2, 3)])
def test_swap_requires_exactly_two_values(pair):
    with pytest.raises(ValueError, match="pair must have exactly 2 values"):
        target.swap(pair)


@pytest.mark.parametrize(
    ("set_a", "set_b", "expected"),
    [
        ({1, 2}, {1, 2}, {1, 2}),
        ({1, 2, 3}, {2, 3, 4}, {2, 3}),
        ({1}, {2}, set()),
        (set(), {1}, set()),
    ],
)
def test_common_items(set_a, set_b, expected):
    result = target.common_items(set_a, set_b)
    assert result == expected
    assert isinstance(result, set)


@pytest.mark.parametrize(
    ("year", "expected"),
    [(1, False), (4, True), (1900, False), (2000, True), (2024, True), (2023, False)],
)
def test_is_leap_year(year, expected):
    assert target.is_leap_year(year) is expected


@pytest.mark.parametrize("year", [0, -1])
def test_is_leap_year_rejects_years_before_one(year):
    with pytest.raises(ValueError, match="year must be 1 or more"):
        target.is_leap_year(year)


@pytest.mark.parametrize(
    ("value", "expected"),
    [(3, 3), ("42", 42), ("-7", -7), (3.9, 3), ("+8", 8)],
)
def test_to_int(value, expected):
    result = target.to_int(value)
    assert result == expected
    assert isinstance(result, int)


def test_to_int_rejects_bool():
    with pytest.raises(TypeError, match="bool is not allowed"):
        target.to_int(True)


@pytest.mark.parametrize(("a", "b", "expected"), [(8, 2, 4), (-9, 3, -3), (1, 2, 0.5), (0, 7, 0)])
def test_divide(a, b, expected):
    assert target.divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="cannot divide by zero"):
        target.divide(1, 0)


@pytest.mark.parametrize(
    ("base", "exponent", "expected"),
    [(2, 3, 8), (2, 0, 1), (2, -2, 0.25), (-2, 3, -8), (9, 0.5, 3.0)],
)
def test_power(base, exponent, expected):
    assert target.power(base, exponent) == expected


@pytest.mark.parametrize(("value", "expected"), [(0, 0), (9, 3), (2.25, 1.5)])
def test_square_root(value, expected):
    assert target.square_root(value) == expected


def test_square_root_negative():
    with pytest.raises(ValueError, match="cannot take the square root of a negative number"):
        target.square_root(-1)


@pytest.mark.parametrize(("number", "expected"), [(0, 1), (1, 1), (5, 120), (10, 3628800)])
def test_factorial(number, expected):
    assert target.factorial(number) == expected


def test_factorial_negative():
    with pytest.raises(ValueError, match="factorial is not defined for negative numbers"):
        target.factorial(-1)


@pytest.mark.parametrize(
    ("numbers", "expected"),
    [([7], 7), ([1, 2, 3], 2), ([-1, 1], 0), ([0, 0], 0), ([1.5, 2.5], 2)],
)
def test_average(numbers, expected):
    assert target.average(numbers) == expected


def test_average_empty_list():
    with pytest.raises(ValueError, match="list is empty"):
        target.average([])

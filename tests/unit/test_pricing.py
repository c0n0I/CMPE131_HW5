import pytest
from src.pricing import (
    parse_price,
    format_currency,
    apply_discount,
    add_tax,
    bulk_total,
)

# parse_price
@pytest.mark.parametrize("text, expected", [
    ("$1,234.50", 1234.50),
    ("12.5", 12.5),
    (" $0.99 ", 0.99),
])
def test_parse_price_valid(text, expected):
    assert parse_price(text) == expected


@pytest.mark.parametrize("text", ["x", "abc", "$12,34,56abc"])
def test_parse_price_invalid(text):
    with pytest.raises(ValueError):
        parse_price(text)


# format_currency
@pytest.mark.parametrize("value, expected", [
    (1, "$1.00"),
    (1.2, "$1.20"),
    (1.234, "$1.23"),
    ("2.5", "$2.50"),
])
def test_format_currency(value, expected):
    assert format_currency(value) == expected


# apply_discount
def test_apply_discount_zero():
    assert apply_discount(100, 0) == 100


def test_apply_discount_large_percent():
    assert apply_discount(100, 2) == 98.0


def test_apply_discount_negative_percent():
    with pytest.raises(ValueError):
        apply_discount(100, -5)


# add_tax
def test_add_tax_default():
    assert add_tax(100) == pytest.approx(107.0)


def test_add_tax_custom():
    assert add_tax(100, 0.1) == pytest.approx(110.0)


def test_add_tax_negative():
    with pytest.raises(ValueError):
        add_tax(100, -0.1)


# bulk_total
def test_bulk_total_simple_list():
    assert bulk_total([10, 10], 0, 0) == 20


def test_bulk_total_with_tax():
    assert bulk_total([10, 20], 0, 0.07) == pytest.approx(32.1)


def test_bulk_total_with_discount():
    assert bulk_total([30, 20], 1, 0.1) == pytest.approx(54.45)

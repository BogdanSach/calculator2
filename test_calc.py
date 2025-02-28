import pytest
from calc import evaluateExpression, ERROR_MSG


@pytest.mark.parametrize(
    "expression, expected_result",
    [
        ("2+3", "5"),
        ("10-4", "6"),
        ("3*7", "21"),
        ("8/2", "4.0"),
        ("10//3", "3"),
        ("10%3", "1"),
        ("2+3*4", "14"),
        ("(5+5)*2", "20"),
        ("100/0", ERROR_MSG),  # Перевірка ділення на 0
        ("abc+1", ERROR_MSG),  # Некоректний вираз
    ],
)
def test_evaluateExpression(expression, expected_result):
    assert evaluateExpression(expression) == expected_result

import pytest
from try_11_03_employee import Employee


@pytest.fixture
def employee():
    return Employee("Jane", "Doe", 10_000)


def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annual_salary == 15_000


def test_give_custom_raise(employee):
    employee.give_raise(7_000)
    assert employee.annual_salary == 17_000

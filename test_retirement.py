import pytest

from retirement import calculate_retirement_date, calculate_retirement_age


def test_calculate_retirement_age_when_birth_year_less_than_1900():
    with pytest.raises(ValueError):
        calculate_retirement_age(-1980)


def test_calculate_retirement_age_when_birth_year_greater_than_equal_3000():
    with pytest.raises(ValueError):
        calculate_retirement_age(3000)


def test_calculate_retirement_age_when_birth_year_is_less_than_1937():
    assert calculate_retirement_age(1936) == (65, 0)


@pytest.mark.parametrize("birth_year", range(1937, 1943))
def test_calculate_retirement_age_when_birth_year_is_between_1937_to_1942(birth_year):
    assert calculate_retirement_age(birth_year) == (65, (birth_year - 1937) * 2)


@pytest.mark.parametrize("birth_year", range(1943, 1954))
def test_calculate_retirement_age_when_birth_year_is_between_1943_to_1953(birth_year):
    assert calculate_retirement_age(birth_year) == (66, 0)


@pytest.mark.parametrize("birth_year", range(1954, 1960))
def test_calculate_retirement_age_when_birth_year_is_between_1954_to_1959(birth_year):
    assert calculate_retirement_age(birth_year) == (66, (birth_year - 1954) * 2)


def test_calculate_retirement_age_when_birth_year_above_1959():
    assert calculate_retirement_age(1971) == (67, 0)


def test_calculate_retirement_date_when_birth_year__less_than_1900():
    with pytest.raises(ValueError):
        calculate_retirement_date(-1980, 12, 65, 5)


def test_calculate_retirement_date_when_birth_year_greater_than_equal_3000() -> object:
    with pytest.raises(ValueError):
        calculate_retirement_date(3000, 12, 65, 5)


def test_calculate_retirement_date_when_birth_month_greater_than_12():
    with pytest.raises(ValueError):
        calculate_retirement_date(1965, 14, 65, 5)


def test_calculate_retirement_date_when_birth_month_less_than_1():
    with pytest.raises(ValueError):
        calculate_retirement_date(1988, -2, 65, 5)


def test_calculate_retirement_date_when_age_year_greater_than_67():
    with pytest.raises(ValueError):
        calculate_retirement_date(1985, 15, 68, 5)


def test_calculate_retirement_date_when_age_year_less_than_65():
    with pytest.raises(ValueError):
        calculate_retirement_date(1956, 4, 63, 5)


def test_calculate_retirement_date_when_age_month_greater_than_12():
    with pytest.raises(ValueError):
        calculate_retirement_date(1981, 10, 68, 29)


def test_calculate_retirement_date_when_age_month_less_than_1():
    with pytest.raises(ValueError):
        calculate_retirement_date(1954, 4, 62, -11)


def test_calculate_retirement_date_for_age_month_plus_birth_month_less_than_equal_12():
    assert calculate_retirement_date(1956, 4, 65, 8) == (2021, 12)


def test_calculate_retirement_date_for_age_month_plus_birth_month_greater_than_12():
    assert calculate_retirement_date(1956, 4, 65, 9) == (2022, 1)
    assert calculate_retirement_date(1956, 4, 65, 9) == (2022, 0)
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
import retirementt

OTHER_TYPES = {
    'Number': int,
}

CONVERSIONS = {
    'birth_year': int,
    'retire_year': int,
    'retire_months': int,
    'birth_month': int,

}

scenarios('../features/retirementt.feature', example_converters=CONVERSIONS)


# 1
# Given Steps

@given('User is new to the retirement calculator ')
def retirement_new():
    pass


# When Steps

@when(parsers.parse('User puts *birth year* into the calculator'))
def user_birth_year(birth_year):
    return birth_year


# Then Steps

@then(parsers.parse('User will be able to see *retirement age* using birth year'))
def retirement_age_results(retirement_age):
    assert retirementt.Retirement.calculateRetirement(retirement_age)


# 2
# Given Steps

@given('User is new to the retirement calculator ')
def retirement_new():
    pass


# When Steps

@when(parsers.parse('User puts *birth month* into the calculator'))
def user_birth_month(birth_month):
    return birth_month


# Then Steps

@then(parsers.parse('User will be able to see *retirement age* using birth month'))
def retirement_age_results(retirement_age):
    assert retirementt.Retirement.calculateRetirement(retirement_age)


# 3
# Given Steps

@given('User inputs birth year into calculator')
def retirement_new(birth_year):
    return birth_year


# When Steps

@when(parsers.parse('User *birth year* is 1937 - 1942'))
def user_birth_year(birth_year):
    year = int(birth_year)
    return year


# Then Steps

@then(parsers.parse('User will see *retirement age* will be 65 years and 0 – 10 months'))
def retirement_age_results(retirement_age):
    assert retirementt.Retirement.retirement(retirement_age)


# 4
# Given Steps

@given('User inputs birth year into calculator')
def retirement_new(birth_year):
    return birth_year


# When Steps

@when(parsers.parse('User *birth year* is 1943 - 1959'))
def user_birth_year(birth_year):
    year = int(birth_year)
    return year


# Then Steps

@then(parsers.parse('User will see *retirement age* will be 66 years and 0 – 10 months'))
def retirement_age_results(retirement_age):
    assert retirementt.Retirement.retirement(retirement_age)


# 5
# Given Steps

@given('User inputs birth year into calculator')
def retirement_new(birth_year):
    return birth_year


# When Steps

@when(parsers.parse('User *birth year* is 1960'))
def user_birth_year(birth_year):
    year = int(birth_year)
    return year


# Then Steps

@then(parsers.parse('User will see *retirement age* will be 67 years'))
def retirement_age_results(retirement_age):
    assert retirementt.Retirement.retirement(retirement_age)


# 6
# Given Steps

@given('User inputs birth month into calculator')
def retirement_new(birth_month):
    return birth_month


# When Steps

@when(parsers.parse('User *birth month* is 0 - 10'))
def user_birth_month(birth_month):
    month = int(birth_month)
    return month


# Then Steps

@then(parsers.parse('User will see *retirement age* months will be between 0 – 10 months'))
def retirement_age_results(retirement_age):
    assert retirementt.Retirement.retirement(retirement_age)


# 7
# Given Steps

@given('User inputs birth year and birth month into calculator')
def retirement_new(birth_year, birth_month):
    return birth_year, birth_month


# When Steps

@when(parsers.parse('Program calculate date of birth'))
def user_birth(birth_year, birth_month):
    year = int(birth_year)
    months = int(birth_month)
    return year, months


# Then Steps

@then(parsers.parse('User will see date of birth'))
def dob_results(dob_result):
    assert retirementt.Retirement.calculateRetirement(dob_result)


# 8
# Given Steps

@given('User inputs birth year into calculator')
def retirement_new(birth_year):
    return birth_year


# When Steps

@when(parsers.parse('Program calculate birth year'))
def user_birth_year(birth_year):
    year = int(birth_year)
    if year != 1:
        return year


# Then Steps

@then(parsers.parse('User will be able to calculate retirement'))
def retirement_results(retirement_age):
    assert retirementt.Retirement.retirement(retirement_age)


# 9
# Given Steps

@given('User inputs birth year into calculator')
def retirement_new(birth_year):
    return birth_year


# When Steps

@when(parsers.parse('Program calculate birth year'))
def user_birth_year(birth_year):
    year = int(birth_year)
    if year == 1:
        return year


# Then Steps

@then(parsers.parse('User will not be able to calculate retirement'))
def retirement_results(retirement_age):
    pytest.fail(retirement_age)

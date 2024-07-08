import pytest

from Module_4.shaskeb4_dice import Die

roll_data = {1, 2, 3, 4, 5, 6}

dice_data = {Die(6), Die(10)}

@pytest.fixture
def my_die():
    return Die(6)


# this isn't a great test, all 6 could pass, all six could fail
# or something between
# this isn't a good test, we want tests that fail only when
# something is wrong
# @pytest.mark.parametrize("roll_results", roll_data)
# def test_roll(my_die, roll_results):
#     value = my_die.roll()
#     assert (value > 0 and value <= my_die.sides)
#     assert (value == roll_results)

# this is a way to use several objects for testing, one after another
@pytest.mark.parametrize("my_dice", dice_data)
def test_roll(my_dice):
    value = my_dice.roll()
    assert (value > 0 and value <= my_dice.sides)
    assert (value == my_dice.getCurrentValue())

# def test_roll(my_die):
#     value = my_die.roll()
#     assert (value > 0 and value <= my_die.sides)
#     assert (value == my_die.getCurrentValue())


def test_get_current_value(my_die):
    value = my_die.roll()
    assert my_die.getCurrentValue() == value


# optional: can test what gets printed to console: https://docs.pytest.org/en/7.1.x/how-to/capture-stdout-stderr.html


# MSOE CSC-5120-301
# Project 6
# Benjamin Shaske, Walter Ziller
# 7.16.2024

# Software Used
# Python V3.12.3
# PyCharm V2024.1.1 (Community)
# PyTest V8.2.2
# ----------------------------------------------------------------------------------------------------------------------

from Reddy_Kilowatt_Ziller import Reddy_Kilowatt
RK = Reddy_Kilowatt  # Create alias for easier slightly less humorous coding.


def test_stab_hertz():
    # Create a character
    char = RK()
    # Assert the razor_sharp_claws result is within expected range
    result = char.stab_hertz()
    assert result >= 0 and result <= 40, f"Expected stab hertz result between 0 and 40, got {result}"


def test_stab_hertz_miss(capsys):
    # Create a character
    char = RK()
    char.name = 'test'
    # Assert the razor_sharp_claws result is within expected range
    result = char.stab_hertz()
    if result == 0:  # what is expected in the event of a miss? text output check.
        captured = capsys.readouterr()
        assert f"{char.name}'s stab hertz attack misses!" in captured.out


def test_thunder_charge(capsys):
    # Create a character
    char = RK()
    char.name = 'test'
    char.thunder_charge()
    captured = capsys.readouterr()
    assert f"{char.name} is charging Thunder!" in captured.out


def test_shock():
    # Create a character
    char = RK()
    # Assert the attack result is within expected range
    result = char.shock()
    assert result >= 0 and result <= 4, f"Expected shock attack result between 0 and 4, got {result}"


def test_thunder():
    # Create a character
    char = RK()
    # Assert the attack result is within expected range
    result = char.thunder()
    assert result >= 0 and result <= 70, f"Expected Thunder attack result between 0 and 70, got {result}"




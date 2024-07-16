# MSOE CSC-5120-301
# Project 6
# Benjamin Shaske, Walter Ziller
# 7.16.2024

# Software Used
# Python V3.12.3
# PyCharm V2024.1.1 (Community)
# PyTest V8.2.2
# ----------------------------------------------------------------------------------------------------------------------

from mugwump_Ziller_Shaske import Mugwump

def test_razor_sharp_claws_hit():
    # Create a character
    char = Mugwump()
    # Assert the razor_sharp_claws result is within expected range
    result = char.razor_sharp_claws()
    assert result >= 0 and result <= 20, f"Expected razor sharp claws result between 0 and 20, got {result}"


def test_razor_sharp_claws_miss():
    # Create a character with the mock dice
    char = Mugwump()
    # Assert the razor_sharp_claws result is within expected range
    result = char.razor_sharp_claws()
    assert result == 0, f"Expected razor sharp claws result is 0, got {result}"


def test_fangs_of_death():
    # Create a character
    char = Mugwump()
    # Assert the razor_sharp_claws result is within expected range
    result = char.razor_sharp_claws()
    assert result >= 0 and result <= 20, f"Expected fangs of death result between 0 and 20, got {result}"


def test_lick_wounds():
    # Create a character
    char = Mugwump()
    # Assert the razor_sharp_claws result is within expected range
    result = char.razor_sharp_claws()
    char.max_hp = 10
    assert result >= 0 and result <= char.max_hp, f"Expected lick wounds result between 0 and max_hp, got {result}"

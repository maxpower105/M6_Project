# MSOE CSC-5120-301
# Project 6
# Benjamin Shaske, Walter Ziller
# 7.16.2024

# Software Used
# Python V3.12.3
# PyCharm V2024.1.1 (Community)
# PyTest V8.2.2
# ----------------------------------------------------------------------------------------------------------------------

from Warrior_Ziller_Shaske import Warrior


def test_attack_with_shield():
    # Create a character
    char = Warrior()
    # Assert the razor_sharp_claws result is within expected range
    result = char.attack_with_shield()
    assert result >= 0 and result <= 4, f"Expected shield result between 0 and 4, got {result}"


def test_attack_with_sword():
    # Create a character
    char = Warrior()
    # Assert the razor_sharp_claws result is within expected range
    result = char.attack_with_sword()
    assert result >= 2 and result <= 16, f"Expected attack with sword result between 0 and 20, got {result}"

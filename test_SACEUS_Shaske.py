# MSOE CSC-5120-301
# Project 6
# Benjamin Shaske, Walter Ziller
# 7.16.2024

# Software Used
# Python V3.12.3
# PyCharm V2024.1.1 (Community)
# PyTest V8.2.2
# ----------------------------------------------------------------------------------------------------------------------

from SACEUS_Shaske import SociallyAwkwardComputerEngineeringUndergradStudent
saceus = SociallyAwkwardComputerEngineeringUndergradStudent  # Create alias for easier slightly less humorous coding.


def test_eye_contact():
    # Create a character
    char = saceus()
    # Assert the razor_sharp_claws result is within expected range
    result = char.eye_contact()
    assert result >= 0 and result <= 40, f"Expected eye contact result between 0 and 40, got {result}"


def test_eye_contact_miss(capsys):
    # Create a character
    char = saceus()
    char.name = 'test'
    # Assert the razor_sharp_claws result is within expected range
    result = char.eye_contact()
    if result == 0:  # what is expected in the event of a miss? text output check.
        captured = capsys.readouterr()
        assert f"{char.name}'s eye contact misses! Looked away at the last second!" in captured.out


def test_magic_the_gathering_charge(capsys):
    # Create a character
    char = saceus()
    char.name = 'test'
    char.magic_the_gathering_charge()
    captured = capsys.readouterr()
    assert f"{char.name} is Soooooooo excited to tell you about Magic the Gathering collection........" in captured.out


def test_nerd_rage():
    # Create a character
    char = saceus()
    # Assert the razor_sharp_claws result is within expected range
    result = char.nerd_rage()
    assert result >= 0 and result <= 4, f"Expected nerd rage result between 0 and 4, got {result}"


def test_magic():
    # Create a character
    char = saceus()
    # Assert the razor_sharp_claws result is within expected range
    result = char.magic()
    assert result >= 0 and result <= 70, f"Expected magic attack result between 0 and 70, got {result}"

# MSOE CSC-5120-301
# Project 4
# Benjamin Shaske
# 6.20.2024

# Software Used
# Python V3.12.3
# PyCharm V2024.1.1 (Community)
# PyTest V8.2.2
# ----------------------------------------------------------------------------------------------------------------------

# Testing (30 pts)
# Install pytest and create tests for all testable functions in battle_sim, mugwump, and die, and include a
# test_filename for each of those 3. The instructor may also provide some tests classes to use/test you code with.
# We used "fixtures" in the sample mugwump test, please use them at least one more time in your tests.
# Try to find a spot to use "parameterization"

""" Import all relevant files. May have an issue. Had to add the sys and od libraries for the sys.path.append line"""
import pytest
import sys
import os

# Add the current directory to the sys.path to correct directory bug
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


from shaskeb4_character import Mugwump
from unittest.mock import patch, MagicMock
# ----------------------------------------------------------------------------------------------------------------------

@pytest.fixture
def mock_mugwump():
    mugwump = Mugwump(True)
    mugwump.d20 = MagicMock()
    mugwump.d6 = MagicMock()
    return mugwump


def test_attack_claws_hit(mock_mugwump, capsys):
    # Setup mock behavior for d20 roll (hit condition for claws)
    mock_mugwump.d20.roll.return_value = 15

    # Setup mock behavior for d6 rolls (simulate 2d6 for claws)
    mock_mugwump.d6.roll.side_effect = [4, 5]  # simulate 2d6 rolls

    # Call the attack method with attack_type 1 (claws)
    damage = mock_mugwump.attack(1)

    # Assert that damage is correct
    assert damage == 9  # 4 + 5 = 9

    # Assert that the correct message was printed
    captured = capsys.readouterr()
    assert "Mugwump hits with claws for 9" in captured.out


def test_attack_claws_miss(mock_mugwump, capsys):
    # Setup mock behavior for d20 roll (miss condition for claws)
    mock_mugwump.d20.roll.return_value = 10

    # Call the attack method with attack_type 1 (claws)
    damage = mock_mugwump.attack(1)

    # Assert that damage is 0 for a miss
    assert damage == 0

    # Assert that the correct message was printed
    captured = capsys.readouterr()
    assert "Mugwump misses with claws" in captured.out


def test_attack_fangs_hit(mock_mugwump, capsys):
    # Setup mock behavior for d20 roll (hit condition for fangs)
    mock_mugwump.d20.roll.return_value = 18

    # Setup mock behavior for d6 rolls (simulate 3d6 for fangs)
    mock_mugwump.d6.roll.side_effect = [3, 4, 5]  # simulate 3d6 rolls

    # Call the attack method with attack_type 2 (fangs)
    damage = mock_mugwump.attack(2)

    # Assert that damage is correct
    assert damage == 12  # 3 + 4 + 5 = 12

    # Assert that the correct message was printed
    captured = capsys.readouterr()
    assert "Mugwump hits with fangs for 12" in captured.out


def test_attack_fangs_miss(mock_mugwump, capsys):
    # Setup mock behavior for d20 roll (miss condition for fangs)
    mock_mugwump.d20.roll.return_value = 14

    # Call the attack method with attack_type 2 (fangs)
    damage = mock_mugwump.attack(2)

    # Assert that damage is 0 for a miss
    assert damage == 0

    # Assert that the correct message was printed
    captured = capsys.readouterr()
    assert "Mugwump misses with fangs" in captured.out


def test_attack_healing(mock_mugwump, capsys):
    # Setup mock behavior for d6 roll (simulate healing)
    mock_mugwump.d6.roll.return_value = 2

    # Call the attack method with attack_type 3 (healing)
    damage = mock_mugwump.attack(3)

    # Assert that damage is correct (negative due to healing)
    assert damage == -2

    # Assert that the correct message was printed
    captured = capsys.readouterr()
    assert "Mugwump heals for 2" in captured.out


# ----------------------------------------------------------------------------------------------------------------------
""" Test for the Mugwump take damage function. """


@pytest.fixture
def sim_Mugwump():
    # Create an instance of the Mugwump class with initial hit points and max hit points
    simulated_mugwump = Mugwump(True)
    simulated_mugwump.hitPoints = 100
    simulated_mugwump.maxHitPoints = 100
    return simulated_mugwump


def test_takeDamage(sim_Mugwump):
    # Test case 1: Damage taken is less than current hit points
    sim_Mugwump.takeDamage(20)
    assert sim_Mugwump.hitPoints == 80  # Check if hit points are correctly reduced

    # Test case 2: Damage taken is equal to current hit points
    sim_Mugwump.takeDamage(80)
    assert sim_Mugwump.hitPoints == 0  # Check if hit points are reduced to 0

    # Test case 3: Damage taken exceeds current hit points
    sim_Mugwump.takeDamage(50)
    assert sim_Mugwump.hitPoints == 0  # Check if hit points remain at 0

    # Test case 4: Damage taken when hit points are initially at maximum
    sim_Mugwump.hitPoints = 100  # Reset hit points to maximum
    sim_Mugwump.takeDamage(120)
    assert sim_Mugwump.hitPoints == 0  # Check if hit points remain at 0

    # Test case 5: Healing scenario where hit points exceed maximum hit points
    sim_Mugwump.hitPoints = 90  # Set hit points close to maximum
    sim_Mugwump.maxHitPoints = 95  # Adjust max hit points
    sim_Mugwump.takeDamage(-10)
    assert sim_Mugwump.hitPoints == 95  # Check if hit points are capped at maxHitPoints

    # Test case 6: No damage scenario
    initial_hit_points = sim_Mugwump.hitPoints
    sim_Mugwump.takeDamage(0)
    assert sim_Mugwump.hitPoints == initial_hit_points  # Check if hit points remain unchanged


# Add more test cases to cover other edge cases and scenarios as needed

# ----------------------------------------------------------------------------------------------------------------------
""" Tes for the __ai function in the mugwump class """


@pytest.fixture
def simulated_d20():
    d20_sim = MagicMock()
    return d20_sim


def test_attack_type(simulated_d20):
    # Create an instance of the class containing the function
    test_mugwump = Mugwump(True)

    # Patch the private attribute __d20 of Monster with simulated_d20
    with patch.object(test_mugwump, 'd20', simulated_d20):
        # Set up simulated roll results for different test cases
        simulated_d20.roll.side_effect = [10, 15, 18]  # Roll values for  test cases

        # Call the function multiple times with different simulated rolls
        attack_type_1 = test_mugwump._Mugwump__ai()  # roll <= 12, expect attack_type = 1
        attack_type_2 = test_mugwump._Mugwump__ai()  # 12 < roll <= 17, expect attack_type = 2
        attack_type_3 = test_mugwump._Mugwump__ai()  # roll > 17, expect attack_type = 3

        # Assert the expected attack types based on the mocked dice rolls
        assert attack_type_1 == 1
        assert attack_type_2 == 2
        assert attack_type_3 == 3

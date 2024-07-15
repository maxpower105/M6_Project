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

from Shaske_Project_4 import shaskeb4_battle_sim as bfs
from Shaske_Project_4.shaskeb4_battle_sim import aiCharacterSelect, characterSelect, playerSelect, initiative
from unittest.mock import patch, MagicMock

# ----------------------------------------------------------------------------------------------------------------------
""" Test for initiative function """


@pytest.fixture
def simulated_d10():
    # Simulating the d10 roll function
    d10_sim = MagicMock()
    d10_sim.roll.side_effect = [6, 3]  # Example rolls for Player 1 and Player 2 initiatives
    return d10_sim


def test_initiative_player1_starts(simulated_d10):  # Verify Player 1 goes first
    with patch('shaskeb4_battle_sim.d10', simulated_d10):
        result = initiative()
        assert result == 1


def test_initiative_player2_goes_first(simulated_d10):  # Verify Player 2 does NOT go first
    with patch('shaskeb4_battle_sim.d10', simulated_d10):
        result = initiative()
        assert result != 2


# ----------------------------------------------------------------------------------------------------------------------
""" Test for player select function """


def test_playerSelect_one_player():
    inputs = iter(['1'])
    with patch('builtins.input', lambda: next(inputs)):
        assert playerSelect() == '1'


def test_playerSelect_two_players():
    inputs = iter(['2'])
    with patch('builtins.input', lambda: next(inputs)):
        assert playerSelect() == '2'


def test_playerSelect_invalid_then_valid():
    inputs = iter(['3', 'one', '2'])
    with patch('builtins.input', lambda: next(inputs)):
        assert playerSelect() == '2'


# ----------------------------------------------------------------------------------------------------------------------
""" Test for Character select. Player should select either a warrior or mugwump. """
@pytest.fixture
def mock_warrior():
    with patch('shaskeb4_battle_sim.bfs.Warrior') as MockWarrior:
        yield MockWarrior


@pytest.fixture
def mock_mugwump():
    with patch('shaskeb4_battle_sim.bfs.Mugwump') as MockMugwump:
        yield MockMugwump


def test_characterSelect_warrior_user(mock_warrior, mock_mugwump):
    inputs = iter(['1', '1'])
    with patch('builtins.input', lambda: next(inputs)):
        player = characterSelect()
        mock_warrior.assert_called_once_with(False)
        mock_mugwump.assert_not_called()
        assert player == mock_warrior.return_value


def test_characterSelect_warrior_ai(mock_warrior, mock_mugwump):
    inputs = iter(['1', '2'])
    with patch('builtins.input', lambda: next(inputs)):
        player = characterSelect()
        mock_warrior.assert_called_once_with(True)
        mock_mugwump.assert_not_called()
        assert player == mock_warrior.return_value


def test_characterSelect_mugwump_user(mock_warrior, mock_mugwump):
    inputs = iter(['2', '1'])
    with patch('builtins.input', lambda: next(inputs)):
        player = characterSelect()
        mock_warrior.assert_not_called()
        mock_mugwump.assert_called_once_with(False)
        assert player == mock_mugwump.return_value


def test_characterSelect_mugwump_ai(mock_warrior, mock_mugwump):
    inputs = iter(['2', '2'])
    with patch('builtins.input', lambda: next(inputs)):
        player = characterSelect()
        mock_warrior.assert_not_called()
        mock_mugwump.assert_called_once_with(True)
        assert player == mock_mugwump.return_value


# ----------------------------------------------------------------------------------------------------------------------
""" Teat for AI character select checking the 50-50 odds via simulated dice roll"""


@pytest.fixture
def simulated_die_roll():
    with patch('shaskeb4_battle_sim.Die') as MockDie:
        mock_die = MockDie.return_value
        yield mock_die


def test_aiCharacterSelect_warrior(simulated_die_roll, mock_warrior, mock_mugwump):
    simulated_die_roll.roll.return_value = 50
    player = aiCharacterSelect()
    mock_warrior.assert_called_once_with(True)
    mock_mugwump.assert_not_called()
    assert player == mock_warrior.return_value


def test_aiCharacterSelect_mugwump(simulated_die_roll, mock_warrior, mock_mugwump):
    simulated_die_roll.roll.return_value = 51
    player = aiCharacterSelect()
    mock_mugwump.assert_called_once_with(True)
    mock_warrior.assert_not_called()
    assert player == mock_mugwump.return_value


# ----------------------------------------------------------------------------------------------------------------------
""" Test cases for the aiCharacterSelect() function in battle sim. Verifies proper input and the .lower function"""


@pytest.fixture
def simulated_input():
    with patch('builtins.input') as mocked_input:
        yield mocked_input


def test_playAgain_yes(simulated_input):
    simulated_input.return_value = 'yes'
    assert bfs.playAgain() == True


def test_playAgain_y(simulated_input):
    simulated_input.return_value = 'y'
    assert bfs.playAgain() == True


def test_playAgain_no(simulated_input):
    simulated_input.return_value = 'no'
    assert bfs.playAgain() == False


def test_playAgain_n(simulated_input):
    simulated_input.return_value = 'n'
    assert bfs.playAgain() == False


def test_playAgain_various_case(simulated_input):
    simulated_input.return_value = 'YeS'
    assert bfs.playAgain() == True
    simulated_input.return_value = 'Y'
    assert bfs.playAgain() == True
    simulated_input.return_value = 'No'
    assert bfs.playAgain() == False
    simulated_input.return_value = 'N'
    assert bfs.playAgain() == False


# ----------------------------------------------------------------------------------------------------------------------
""" Attempt to use a parameterize test. Pass in Yes then y for True conditions, no and n for false conditions. """


@pytest.mark.parametrize("input_data", ["yes", "y", "no", "n"])
def test_play_again(input_data, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: input_data)
    result = bfs.playAgain()
    assert result == (input_data.lower() in ['yes', 'y'])
    assert result != (input_data.lower() in ['no', 'n'])

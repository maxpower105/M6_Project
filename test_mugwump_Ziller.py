def test_attack(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 1)
    attack_choice = int(input("Enter choice: "))
    assert attack_choice == 1


from mugwump_Ziller import Mugwump
from die_Ziller import Die
import pytest

def test_mugwump(): # test ai function using a seed

    # Test function for __ai method
    # Change ai from hidden to public in order to test
    def test_ai_razor_sharp_claws():
        mugwump = Mugwump()
        mugwump.d20 = Die(20, seed=1)  # Setting a seed to get predictable results
        assert mugwump._Mugwump__ai() == 1  # Expected result based on the seed

    def test_ai_fangs_of_death():
        mugwump = Mugwump()
        mugwump.d20 = Die(20, seed=2)  # Setting a seed to get predictable results
        assert mugwump._Mugwump__ai() == 2  # Expected result based on the seed

    def test_ai_heal():
        mugwump = Mugwump()
        mugwump.d20 = Die(20, seed=3)  # Setting a seed to get predictable results
        assert mugwump._Mugwump__ai() == 3  # Expected result based on the seed

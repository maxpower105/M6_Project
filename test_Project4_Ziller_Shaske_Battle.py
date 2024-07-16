# MSOE CSC-5120-301
# Project 6
# Benjamin Shaske, Walter Ziller
# 7.16.2024

# Software Used
# Python V3.12.3
# PyCharm V2024.1.1 (Community)
# PyTest V8.2.2
# ----------------------------------------------------------------------------------------------------------------------

def test_victory(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "y")
    choice = input("Would you like to play again (yes/no)? ")
    assert choice == "y"

def test_victory(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Y")
    choice = input("Would you like to play again (yes/no)? ")
    assert choice == "y"

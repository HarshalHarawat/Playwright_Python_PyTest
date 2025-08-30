import pytest


@pytest.mark.regression
def test_secondmeth():
    print("Validating Second method")

def test_fourthmeth(sesssionfixtures):
    print("Validating fourth method")


def creds():
    return [
        ("harshal", "Harawat"),
        ("divya", "jain"),
        ("hetu", "harawat")
    ]

@pytest.mark.parametrize("username,password", creds())
def test_dologin(username, password):
    print(username, "----", password)

import pytest

@pytest.fixture(scope="function")
def functionfixtures():
    print("Execute before each function")
    return "returning the value in function scope"


@pytest.fixture(scope="module")
def modulefixtures():
    print("Execute only once for 1 .py file")
# -------------------------------------------------

def test_firstmethod(functionfixtures,modulefixtures,sesssionfixtures):
    print("This is my first method for validation!!!")
    print(functionfixtures)

def test_secondmethod(functionfixtures,modulefixtures):
    print("This is my second method for validation!!!")
    print(functionfixtures)

def test_thirdmethod(functionfixtures):
    print("this is my third method for validation")
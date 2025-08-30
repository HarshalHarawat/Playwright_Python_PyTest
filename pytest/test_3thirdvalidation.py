import pytest

@pytest.fixture(scope="function")
def setupTeardown():
    print("this is our set up for execution")
    yield
    print("team down method")

def test_firstTestcase(setupTeardown):
    print("Executed first test case")

def test_secondTestcase(setupTeardown):
    print("Executed second test case")

@pytest.mark.skip
def test_thirdTestcase():
    print("Executed third test case")

@pytest.mark.smoke
def test_fourthTestcase():
    print("Executed fourth test case")


import pytest

@pytest.fixture(scope="session")
def sesssionfixtures():
    print("Session:---Execute one setup for everything")
    yield  # pause
    print("********closing the window at the end of session******")
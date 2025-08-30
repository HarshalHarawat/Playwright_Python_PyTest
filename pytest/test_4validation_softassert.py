

def test_myfilevalidation():
    expected = "harshal"
    actual = "harsha"

    assert actual == expected , "both are not equal"
    assert "ar" in actual , "ar not present in actual"
    assert False , "Forefully failing "
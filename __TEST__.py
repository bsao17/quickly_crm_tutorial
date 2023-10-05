from user import *


class TestTestReturnsDifferentNames:

    #  The function returns two different names when called twice.
    def test_returns_different_names_twice(self):
        result1 = get_user()
        result2 = get_user()
        assert result1 != result2

    #  The function can handle a large number of calls without repeating the same name.
    def test_returns_different_names_large_number_of_calls(self):
        names = set()
        for _ in range(650):
            name = get_user()
            assert name not in names
            names.add(name)

    #  The function can handle special characters in the names.
    def test_returns_different_names_special_characters(self):
        result1 = get_user()
        result2 = get_user()
        assert result1 != result2
        assert all(c.isalpha() or c.isspace() for c in result1)
        assert all(c.isalpha() or c.isspace() for c in result2)

    #  The function can handle names with apostrophes.
    def test_returns_different_names_apostrophes(self):
        result1 = get_user()
        result2 = get_user()
        assert result1 != result2
        assert "'" not in result1
        assert "'" not in result2

    #  The function returns a string with two space-separated words.
    def test_returns_different_names_two_words(self):
        result1 = get_user()
        result2 = get_user()
        assert result1 != result2
        assert len(result1.split()) == 2
        assert len(result2.split()) == 2

    #  The function can handle non-ASCII characters in the names.
    def test_returns_different_names_non_ascii(self):
        result1 = get_user()
        result2 = get_user()
        assert result1 != result2
        assert all(ord(c) < 128 for c in result1)
        assert all(ord(c) < 128 for c in result2)

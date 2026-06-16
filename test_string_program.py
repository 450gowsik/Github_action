from string_program import StringTools

tool = StringTools()

def test_reverse():
    assert tool.reverse("hello") == "olleh"

def test_uppercase():
    assert tool.uppercase("abc") == "ABC"

def test_lowercase():
    assert tool.lowercase("HELLO") == "hello"

def test_words():
    assert tool.count_words("hello world") == 
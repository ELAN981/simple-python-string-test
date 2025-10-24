
import pytest
import spellcheck


alpha = "Checking the length and structure of the sentence."
beta = "this sentence should fail a test case"

@pytest.fixture
def input_val():
    input = alpha
    return input

def test_length(input_val):
    assert spellcheck.word_count(input_val) < 10 
    assert spellcheck.char_count(input_val) < 50

def test_struc(input_val):
    assert spellcheck.first_char(input_val).isupper() == True
    assert spellcheck.last_char(input_val) == '.'


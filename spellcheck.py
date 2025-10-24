def word_count(sentence):
    """
    Counts the number of words in a given sentence.

    Parameters:
    sentence (str): The input sentence.

    Returns:
    int: The number of words in the sentence.
    """
    words = sentence.split()
    return len(words)

def char_count(sentence):
    chars = len(sentence.split())
    print(f"Number of characters: {chars}")
    return chars

def first_char(sentence):
    first_char = sentence[0]
    if not first_char:
        print("not upper case")
    print(f"the first letter {first_char} is uppper case")
    #print(first_char)
    return first_char

def last_char(sentence):
    last_char = sentence[-1]
    #print(last_char)
    return last_char
 
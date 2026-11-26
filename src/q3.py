from q1 import num_letters


def num_vowels(word):
    """Count the vowels in word, including y when it acts as a vowel.

    Precondition: word is a string made only of letters (it may be empty).
    An AssertionError is raised otherwise.

    Returns an int. a, e, i, o and u always count, ignoring case.
    If the word has none of those, every y counts. Otherwise a y counts
    unless the letter right after it is a, e, i, o or u.
    """
    # Guardian 1: the input must be a string.
    assert type(word) == str, "word must be a string"


    # Guardian 2: every character must be an English letter (a-z, any case).
     # An empty word passes because the loop never runs.
     
    # English letters (a-z)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for character in word:
     
         assert character.lower() in alphabet, "word must contain only letters"

    #   converting to lower case
    word = word.lower()

    # Count the normal vowels with the function from Part 1.
    count = num_letters(word, "aeiou")

    if count == 0:
        # Rule A: no other vowels, so every y is a vowel.
        count = num_letters(word, "y")
    else:
        # Rule B: a y is a vowel unless the next letter is a vowel.
        position = 0
        while position < len(word):
            if word[position] == "y":
                # Check there is a next letter before reading it, so a
                # y at the end of the word doesn't cause an IndexError.
                is_last = position + 1 == len(word)
                if is_last or word[position + 1] not in "aeiou":
                    count += 1
            position += 1

    return count

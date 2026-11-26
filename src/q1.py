def num_letters(text, letters):
    """Count how many characters in text are one of the given letters.

    Precondition: text and letters are both strings.

    Returns an int: the number of positions in text whose character
    appears anywhere in letters. Upper and lower case are treated as
    the same, a letter repeated in letters is only counted once, and
    the result is 0 if either string is empty.
    """
    # if text or letters is empty, return 0
    if text == "" or letters == "":
        return 0

    # convert text and letters to lowercase
    text = text.lower()
    letters = letters.lower()

    count = 0
    position = 0
    while position < len(text):
        # check if the character in text is in letters
        if text[position] in letters:
            count += 1
        position += 1
    return count

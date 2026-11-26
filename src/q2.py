def num_letters(text, letters):
    """Count how many characters in text are one of the given letters.

    Precondition: text and letters are both strings.

    Returns an int: the number of characters in text that appear
    anywhere in letters. Upper and lower case are treated as the same,
    a letter repeated in letters is only counted once, and the result
    is 0 if either string is empty.
    """
    # Nothing to search in, or nothing to look for.
    if text == "" or letters == "":
        return 0

    # Lowercase both so that capitals match too.
    letters = letters.lower()

    count = 0
    # Go through text one character at a time.
    for character in text.lower():
        
        # duplicate check
        if character in letters:
            count += 1
    return count

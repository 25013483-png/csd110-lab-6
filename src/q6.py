from q5 import shift


def cipher(text, amount):
    """Return the Caesar cipher of text, using the given shift amount.

    Precondition: text is a string and amount is an int.

    Each letter is replaced by the letter at the same position in the
    alphabet after it has been shifted by amount (using shift from Part 5).
    Upper case letters stay upper case, lower case letters stay lower case,
    and anything that is not a letter (spaces, digits, punctuation) is
    copied over unchanged.
    """
    # Guardians: check the types of both parameters.
    assert type(text) == str, "text must be a string"
    assert type(amount) == int, "amount must be an int"

    # The normal alphabet, and the same alphabet shifted by amount.
    # Letter number i in plain_lower is encrypted as letter number i
    # in shifted_lower. Upper case versions keep capitals as capitals.
    plain_lower = "abcdefghijklmnopqrstuvwxyz"
    shifted_lower = shift(plain_lower, amount)
    plain_upper = plain_lower.upper()
    shifted_upper = shifted_lower.upper()

    encrypted = ""
    # Encrypt the text one character at a time.
    for character in text:
        if character in plain_lower:
            # Find where the letter sits in the normal alphabet, then take
            # the letter at that same position in the shifted alphabet.
            position = plain_lower.index(character)
            encrypted += shifted_lower[position]
        elif character in plain_upper:
            position = plain_upper.index(character)
            encrypted += shifted_upper[position]
        else:
            # Not a letter, so it stays as it is.
            encrypted += character
    return encrypted


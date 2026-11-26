def shift(text, amount):
    """Return a copy of text with its characters rotated by amount places.

    Precondition: text is a string and amount is an int.

    A positive amount moves characters to the right and a negative amount
    moves them to the left. Characters that fall off one end wrap around
    to the other, so the result is always the same length as text.
    """
    # Guardians: check the types of both parameters.
    assert type(text) == str, "text must be a string"
    assert type(amount) == int, "amount must be an int"

    # An empty string has nothing to shift (and len 0 would make % fail).
    if text == "":
        return ""

    # Shifting by a multiple of the length gives back the same string, so
    # only the remainder matters. % also turns a negative shift into the
    # equivalent right shift, e.g. -1 % 6 == 5.
    amount = amount % len(text)

    # The last `amount` characters move to the front.
    split = len(text) - amount
    return text[split:] + text[:split]


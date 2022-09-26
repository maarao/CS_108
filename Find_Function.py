from bakery import assert_equal
def in_text(character:str, text:str)->str:
    if not text:
        return None
    elif character == text[0]:
        return character
    else:
        return in_text(character, text[1:])

assert_equal(in_text("k", "aka"), "k")
assert_equal(in_text("k", ""), None)
assert_equal(in_text("k", "abc"), None)
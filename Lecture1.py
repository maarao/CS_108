from bakery import assert_equal

def process_str(text:str):
    if not text:
        return
    else:
        print(text[0])
        process_str(text[1:])

def cap_letter(char: str) -> str:
    return char.upper()


# 1
def map(fcn, text:str):
    if text:
        return fcn(text[0]) + map(fcn, text[1:])
    else:
        return text

assert_equal(map(cap_letter, "abc"), "ABC")

# 2

def letter_plus(letter:str, number:int)->str:
    shift = ord(letter[0]) + number
    if shift > 90:
        shift -= 26
    return chr(shift)

def caesar_cipher(fcn, text:str, shift:int)->str:
    if text:
        return fcn(text[0] + caesar_cipher(fcn, text[1:shift])

assert_equal(letter_plus("A", 3), "D")
assert_equal(letter_plus("Z", 1), "A")
print(ord("Z"))
print(ord("A"))
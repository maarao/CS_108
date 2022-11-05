from bakery import assert_equal


def rotate(char_int: int, rotation: int) -> str:
    """
    Helper function to rotate a single character a specified amount

    Parameters:
    char_int (integer): character in integer form that should be rotated
    rotation (integer): the amount the integer should be rotated by

    Returns a string with the character rotated
    """
    rotated = ((char_int + rotation - 32) % 94 + 32)
    if rotated <= 48:
        return chr(rotated) + "~"
    else:
        return chr(rotated)


def encrypt_text(message: str, rotation: int) -> str:
    """
    Encrypts a string

    Parameters:
    message (string): the message that should be encrypted
    rotation (integer): the amount every character in the message should be rotated by

    Returns a string with the message in encrypted form
    """
    encrypted = ""
    for char in message:
        encrypted += rotate(ord(char), rotation)
    return encrypted


def decrypt_text(message: str, rotation: int) -> str:
    """
    Decrypts a string

    Parameters:
    message (string): the message that should be decrypted
    rotation (integer): the amount every character in the message was rotated when encrypted

    Returns a string with the message in decrypted form
    """
    encrypted_int = []
    for char in message:
        encrypted_int.append(ord(char))
    filtered = []
    for i in encrypted_int:
        if not i == 126:
            filtered.append(i)
    decrypted = ""
    for char_int in filtered:
        decrypted += (chr((char_int - rotation - 32) % 94 + 32))
    return decrypted


assert_equal(encrypt_text("ABC", 1), "BCD")
assert_equal(decrypt_text("BCD", 1), "ABC")


def hash_text(message: str, base: int, hash_size: int) -> int:
    """
    Finds the hash value of text

    Parameters:
    message (string): the message that the function will find the hash value on
    base (integer): an arbitrarily chosen number that will be added to the index
    hash_size (integer): the number to limit the total value to

    Returns an integer that attempts to uniquely represent the text
    """
    converted = []
    for char in message:
        converted.append(ord(char))
    total = 0
    for index, value in enumerate(converted):
        total += (index + base) ** value
    return total % hash_size


assert_equal(hash_text("CAT", 31, 10 ** 9), 146685664)
assert_equal(hash_text("A", 11, 100), 51)


def main():
    """
    """
    answer = input("Input your desired action: ")
    if answer == "encrypt":
        plaintext = input("Input your plaintext message: ")
        encrypted = encrypt_text(plaintext, 10)
        hashed = hash_text(plaintext, 31, 1000000000)
        print(encrypted, hashed)
    elif answer == "decrypt":
        encrypted = input("Input your encrypted message: ")
        decrypted = decrypt_text(encrypted, 10)
        guess = input("Guess the expected hash:")
        if hash_text(decrypted, 31, 1000000000) == int(guess):
            print(decrypted)
        else:
            print("Error in your calculations")
    else:
        print("Not an option")


main()

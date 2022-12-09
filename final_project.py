from bakery import assert_equal
# from tkinter import filedialog
# from tkinter import *
from PIL import Image

#############################################################
"""
NOTA BENE: Do not change the names, parameters, or return types of these functions.
They must stay the same to pass our tests.
NOTA BENE SECUNDUS: You have already written variations of these functions. Use 
your work!
"""
"""
TO USE:
Call encode(msg, image) on a secret message file and an image filename
The new image (a .png file) has the secret message hidden inside (steganography!).
Call decode(image) to see the secret message again. 
Encoding preserves A-Z and '\n. ,?'
"""
"""
TO START:
Identify low-level functions that can be written and tested without calling other 
functions. Write and test these first (comment out the other tests). Then look for 
reciprocal functions that you can write and test against each other (see tests 
provided). As you write tests and gain understanding about a function, feel free to
add to its comments!
"""
"""
REQUIRED:
For each function, write at least THREE additional good tests. Your tests should 
not rely on external files -- create files in code when needed (see tests 
provided). Look for boundary conditions not already being tested. Use the best 
coding style we have learned in class, it will be graded.
"""
#############################################################
TEST = True
"""Please don't alter the next three lines"""
char_codes_strip = {'\n': 91, '.': 92, ' ': 93, ',': 94, '?': 96}  # strip out underscore
charCodesEncode = {**char_codes_strip, '_': 95}  # allow underscore for encoding, decoding
inverseCharCodes = {value: key for key, value in charCodesEncode.items()}  # use when decoding
"""
Read image
Get pixel array
Get message (from file or input)
Strip message
Prepare message x
Walk pixels, inserting chars
Save image as .png
___
Get filename
Open image
Get pixels
Walk pixels and get message
restore message
return message
"""


def decode(image_file_name):
    """
    Open image, get chars from image
    Call select_msg_output to allow user to choose what to do with message
    Also calls restore, get_msg_from_image.  No automated tests for this function.
    """
    image = Image.open(image_file_name)
    select_msg_output(restore_msg(get_msg_from_image(image)))


#
def select_msg_output(msg):
    """
    Ask user whether to print (p), save (s), or return (default) message, then
perform. Should be able to handle input with leading or trailing whitespace. No
automated tests for this function.
    """
    choice = input("Would you like to print (p), save (s), or return the message: ")
    if choice == "p":
        print(msg)
    elif choice == "s":
        with open('decoded_msg.txt', 'w') as ofile:
            ofile.write(msg)
    else:
        return msg


#
def restore_msg(string):
    """
    Replace underscores with spaces; trim trailing characters off the end.
    """
    replaced = ""
    for c in string:
        if c == "_":
            replaced += " "
        else:
            replaced += c
    return replaced


#
#
def get_msg_from_image(image1):
    """
    Go through pixels in the image and extract chars until the message
    is finished. Calls get_char_from_color.  Only process pixels until
    the end of the message. If message is not properly terminated, print an error
message.
    """
    message = ""
    count_underscores = 0
    for y in range(image1.height):
        for x in range(image1.width):
            char = get_char_from_color(image1.getpixel((x, y)))
            if char == "_":
                count_underscores += 1
                message += " "
            else:
                message += char
                count_underscores = 0
            if count_underscores >= 3:
                return message[:-3]
    print("ERROR: Not Terminated properly")


#
def encode(message_file_name, image_file_name):
    """
    Gets the message and prepares it for encoding
    Gets the image information and opens it, copies it
    Checks that image is big enough to hold message, prints error message if not
    Put every char from message into image
    Save resulting image with new name (get_new_file_name())
    return new image
    """
    text = prepare_message(strip_message(open(message_file_name).read()))
    convert = Image.open(image_file_name)
    if convert.width * convert.height >= len(text):
        filename = get_new_file_name(image_file_name)
        put_all_chars_in_image(convert, text).save(filename)
        return Image.open(filename)
    else:
        print("ERROR: Image is not big enough to hold the message")


def get_new_file_name(old):
    """
    Change the old file name to end with '.encoded.png'
    e.g. 'spam.png' -> 'spam.encoded.png' OR 'spam.jpeg' -> 'spam.encoded.png'
    """
    return old[0:-4] + ".encoded" + old[-4:]


def put_all_chars_in_image(image1, msg):
    """
    Takes an opened image and a fully processed message
    Encodes the message into the image, one char to each pixel
(put_one_char_in_colors())
    Returns the image
    """
    count = 0
    for y in range(image1.height):
        for x in range(image1.width):
            image1.putpixel((x, y), put_one_char_in_colors(image1.getpixel((x, y)), msg[count]))
            count += 1
            if count == len(msg):
                return image1


def get_message_from_file(message_file_name):
    msg = None
    with open(message_file_name, 'r') as infile:
        msg = infile.read()
    return msg


def strip_message(strin):
    """
    Returns a string with all unacceptable chars removed.
    May only look at each char in the input string once. USE THE STRIP DICTIONARY
PROVIDED AT TOP.
    Acceptable characters: AZaz\n. ,?
    """
    final = ""
    for c in strin:
        numchar = ord(c)
        if (c in char_codes_strip) or ((numchar >= 65 and numchar <= 90) or (numchar >= 97 and numchar <= 122)):
            final += c
    return final


def prepare_message(input_string: str):
    """
    Convert parameter string to upper case and replace any spaces with underscores.
Any occurrence of consecutive spaces should be replaced with a single underscore
(CALL THE FUNCTION YOU WROTE). Add a sequence of three underscores to the end of
the message '___'.
    https://docs.python.org/3/library/stdtypes.html#textseq
    """
    final = ""
    last_char = input_string[0]
    for c in input_string:
        if not (last_char == " " and c == " "):
            final += c
        last_char = c
    return final.upper().replace(" ", "_") + "___"


def put_one_char_in_colors(color, char):
    """
    Get ASCII value of uppercase character (for special characters use
charCodesEncode), change to A=0 base. Then convert 2 digit base 10 to base 6. Put
first digit of into last digit of G, and second into last digit of B.
assert_equal( put_one_char_in_colors(color1, 'Z'), (255, 254, 251))
    color  -- RGB triple
    char   -- ASCII char
    return -- color 3-tuple with char hidden inside
    """
    char_ord = 0
    if char in charCodesEncode:
        char_ord = charCodesEncode[char] - 65
    else:
        char_ord = ord(char) - 65

    return color[0], (color[1] // 10) * 10 + char_ord // 6, (color[2] // 10) * 10 + char_ord % 6


def get_char_from_color(color):
    """
    Get two digits from color 3-tuple, translate to base 10, add 65, convert to
char.
    Use inverseCharCodes.
    """
    char_ord = color[1] % 10 * 6 + color[2] % 10 + 65

    char = ''
    if char_ord in inverseCharCodes:
        char = inverseCharCodes[char_ord]
    else:
        char = chr(char_ord)
    return char


if TEST:
    assert_equal(strip_message('AaZz\n. ,?'), 'AaZz\n. ,?')
    assert_equal(strip_message('2190!@#$-=+<>;":_'), '')
    # My Tests
    assert_equal(strip_message("3289723497"), "")
    assert_equal(strip_message("!^&@&@^A"), "A")
    assert_equal(strip_message("!^&@&@^A123123123"), "A")

    assert_equal(prepare_message("I once had a dog"), "I_ONCE_HAD_A_DOG___")
    assert_equal(prepare_message("I  once    had   a    dog"), "I_ONCE_HAD_A_DOG___")
    assert_equal(prepare_message("I  once    had\n   a       dog"), "I_ONCE_HAD\n_A_DOG___")
    # My Tests
    assert_equal(prepare_message("This is cool"), "THIS_IS_COOL___")
    assert_equal(prepare_message("This     is     cool"), "THIS_IS_COOL___")
    assert_equal(prepare_message("Im     having     fun!"), "IM_HAVING_FUN!___")

    # Jackson
    assert_equal(prepare_message('This should be line 1\n this should be line 2'),
                 'THIS_SHOULD_BE_LINE_1\n_THIS_SHOULD_BE_LINE_2___')
    # My Tests
    assert_equal(prepare_message("One line\nAnother line"), "ONE_LINE\nANOTHER_LINE___")
    assert_equal(prepare_message(" So does this work\n Here is a space"), "SO_DOES_THIS_WORK\n_HERE_IS_A_SPACE___")
    assert_equal(prepare_message("ALL CAPS"), "ALL_CAPS___")

    color1 = (255, 255, 255)
    assert_equal(put_one_char_in_colors(color1, 'A'), (255, 250, 250))
    assert_equal(put_one_char_in_colors(color1, '?'), (255, 255, 251))
    assert_equal(put_one_char_in_colors(color1, 'Z'), (255, 254, 251))
    assert_equal(put_one_char_in_colors(color1, '_'), (255, 255, 250))
    # My Test
    assert_equal(put_one_char_in_colors(color1, 'B'), (255, 250, 251))
    assert_equal(put_one_char_in_colors(color1, 'C'), (255, 250, 252))
    assert_equal(put_one_char_in_colors(color1, 'D'), (255, 250, 253))

    assert_equal(get_char_from_color((255, 250, 250)), 'A')
    assert_equal(get_char_from_color((0, 5, 1)), '?')
    assert_equal(get_char_from_color((0, 5, 0)), '_')
    assert_equal(get_char_from_color((55, 254, 251)), 'Z')
    # My Test
    assert_equal(get_char_from_color((0, 0, 0)), "A")
    assert_equal(get_char_from_color((0, 0, 1)), "B")
    assert_equal(get_char_from_color((0, 0, 2)), "C")

    for i in range(0, 256, 5):
        color = (i, i, i)
        for c in charCodesEncode:
            color = put_one_char_in_colors(color, c)
            assert_equal(get_char_from_color(color), c)

        for c in 'AZ':
            color = put_one_char_in_colors(color, c)
            assert_equal(get_char_from_color(color), c)
        # My Tests
        assert_equal(get_char_from_color(put_one_char_in_colors((0, 0, 0), "A")), "A")
        assert_equal(get_char_from_color(put_one_char_in_colors((0, 0, 0), "?")), "?")
        assert_equal(get_char_from_color(put_one_char_in_colors((0, 0, 0), "_")), "_")


    assert_equal(strip_message("Hey!"), "Hey")
    assert_equal(strip_message("Test: 'quote?'"), "Test quote?")
    assert_equal(strip_message("This should all work."), "This should all work.")
    assert_equal(strip_message("Un@ccept@ble Str!ng"), "Uncceptble Strng")

    # My Test
    assert_equal(strip_message("@!#$"), "")
    assert_equal(strip_message("ASD"), "ASD")
    assert_equal(strip_message("asd4"), "asd")


    def compare(im1, im2):
        if im1.size != im2.size:
            return False
        else:
            p1 = im1.load()
            p2 = im2.load()
            for r in range(im1.size[1]):
                for c in range(im1.size[0]):
                    if p1[c, r] != p2[c, r]:
                        return False
        return True


    image0 = Image.new('RGB', (2, 1), (0, 0, 0))
    image0 = put_all_chars_in_image(image0, "AZ")
    pixels0 = image0.load()
    assert_equal(pixels0[0, 0], (0, 0, 0))
    assert_equal(pixels0[1, 0], (0, 4, 1))
    image0 = Image.new('RGB', (3, 2), (0, 0, 0))
    image1 = image0.copy()
    image1 = put_all_chars_in_image(image1, "AZ?___")
    pixels0 = image0.load()
    pixels0[0, 0] = (0, 0, 0)
    pixels0[1, 0] = (0, 4, 1)
    pixels0[2, 0] = (0, 5, 1)
    pixels0[0, 1] = (0, 5, 0)
    pixels0[1, 1] = (0, 5, 0)
    pixels0[2, 1] = (0, 5, 0)
    assert_equal(compare(image0, image1), True)
    image0 = Image.new('RGB', (3, 2), (0, 0, 0))
    image0.save('temp.png')
    with open('msg.txt', 'w') as ofile:
        ofile.write("AZ?___")
    new_im1 = encode('msg.txt', 'temp.png')
    pixels0 = image0.load()
    pixels0[0, 0] = (0, 0, 0)
    pixels0[1, 0] = (0, 4, 1)
    pixels0[2, 0] = (0, 5, 1)
    pixels0[0, 1] = (0, 5, 0)
    pixels0[1, 1] = (0, 5, 0)
    pixels0[2, 1] = (0, 5, 0)
    assert_equal(compare(image0, new_im1), True)
    image0 = Image.new('RGB', (6, 1), (0, 0, 0))
    image0.save('temp.png')
    with open('msg.txt', 'w') as ofile:
        ofile.write("AZ?___")
    new_im2 = encode('msg.txt', 'temp.png')
    pixels0 = image0.load()
    pixels0[0, 0] = (0, 0, 0)
    pixels0[1, 0] = (0, 4, 1)
    pixels0[2, 0] = (0, 5, 1)
    pixels0[3, 0] = (0, 5, 0)
    pixels0[4, 0] = (0, 5, 0)
    pixels0[5, 0] = (0, 5, 0)
    assert_equal(compare(image0, new_im2), True)
    assert_equal(restore_msg(get_msg_from_image(new_im2)), 'AZ?')
    assert_equal(restore_msg(get_msg_from_image(new_im1)), 'AZ?')

    image0 = Image.new('RGB', (500, 500), (0, 0, 0))
    image0.save('temp4.png')
    with open('msg4.txt', 'w') as ofile:
        ofile.write("A" * (500 * 500 - 3))
        ofile.write('___')
    new_im4 = encode('msg4.txt', 'temp4.png')
    assert_equal(restore_msg(get_msg_from_image(new_im4)), 'A' * (250000 - 3))


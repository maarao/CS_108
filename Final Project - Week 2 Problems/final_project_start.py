from PIL import Image, ImageDraw, ImageColor
from bakery import assert_equal

# Question 4
animal_noises = {'cow': 'moo', 'pig': 'oink', 'sheep': 'baa', 'dog': 'woof', 'cat': 'meow', 'bird': 'chirp'}
print(animal_noises)


# Question 5
def count_animals(animals: [str]):
    animal_count = {}
    for a in animals:
        if a not in animal_count:
            animal_count[a] = 1
        else:
            animal_count[a] += 1
    return animal_count


assert_equal(count_animals(['echidna', 'echidna', 'wombat', 'echidna']), {'echidna': 3, 'wombat': 1})
assert_equal(count_animals(['echidna', 'echidna', 'wombat', 'echidna', 'wombat', 'wombat']),{'echidna': 3, 'wombat': 3})
assert_equal(count_animals(['echidna','echidna','wombat','echidna','wombat','wombat','wombat','wombat']),{'echidna':3,'wombat':5})


# Question 6 - {'\n': 13427, '.': 6396, ' ': 113927, ',': 9280, '?': 462}
def myReadFcn(filename):
    """
    filename -- string
    """

    with open(filename,'r') as infile:
        data = infile.read()

    char_count = {'\n': 0, '.': 0, ' ': 0, ',': 0, '?': 0}
    for d in data:
        if d in char_count:
            char_count[d] += 1
    return char_count


assert_equal(myReadFcn("minijane1.txt"), {'\n': 8, '.': 3, ' ': 54, ',': 2, '?': 0})
assert_equal(myReadFcn('minijane2.txt'), {'\n': 7, '.': 3, ' ': 76, ',': 6, '?': 1})
assert_equal(myReadFcn('minijane3.txt'), {'\n': 15, '.': 8, ' ': 124, ',': 8, '?': 3})


# Question 7
def reduced_to_one(char, text):
    count = 0
    removed = ''
    for t in text:
        if char == t:
            count += 1
            if count <= 1:
                removed += t
        else:
            count = 0
            removed += t
    return removed


assert_equal(reduced_to_one('a', 'aaababa'), 'ababa')


# Question 8
def base_six(base_10):
    base_6 = str(base_10 // 6) + str(base_10 % 6)

    return base_6

assert_equal(base_six(19), '31')


# Question 9
def solid_rectangle(image):
    draw = ImageDraw.Draw(image)
    draw.rectangle([(200, 200), (1000, 1000)], "red", 5)
    image.show()


solid_rectangle(Image.open("image.JPG"))


# Question 10
def clamp(num, min_value, max_value):
    return max(min(num, max_value), min_value)


def mod_image(filename: str, delta: int, colorstring: str) -> Image:
    image = Image.open(filename)
    for x in range(image.width):
        for y in range(image.height):
            rgb = image.getpixel((x, y))
            r = rgb[0]
            g = rgb[1]
            b = rgb[2]
            for c in colorstring:
                if c == "r":
                    r = clamp(rgb[0]+delta, 0, 255)
                elif c == "g":
                    g = clamp(rgb[0]+delta, 0, 255)
                elif c == "b":
                    b = clamp(rgb[0]+delta, 0, 255)
            new_rgb = (r, g, b, 255)
            image.putpixel((x, y), new_rgb)
    return image


mod_image("image.JPG", 255, 'r').show()
mod_image("image.JPG", 255, 'b').show()
mod_image("image.JPG", -255, 'r').show()
mod_image("image.JPG", -255, 'g').show()

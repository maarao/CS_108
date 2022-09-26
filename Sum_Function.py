from bakery import assert_equal
def summation(ints):
    if not ints:
        return 0
    else:
        return ints[0] + summation(ints[1:])

assert_equal(summation([1, 2, 3]), 6)
assert_equal(summation([]), 0)
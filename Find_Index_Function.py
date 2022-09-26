from bakery import assert_equal
def find_index(aint:int, alist:list[int])->int:
    if not alist:
        return None
    elif aint == alist[0]:
        return 0
    else:
        result = find_index(aint, alist[1:])
        if result != None:
            return 1 + result

assert_equal(find_index(3, [1, 2, 3, 4]), 2)
assert_equal(find_index(5, [1, 2, 3, 4]), None)
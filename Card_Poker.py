from bakery import assert_equal
# do not delete the above line

def convert_hand(card:int)->str:
    """
    Converts a single integer to the appropriate card string

    Args:
    Card (integer) - The card number

    Returns a string containing the correct card name.

    """

    # If it is greater than 10, it is not represented normally
    if card >= 10:
        if card == 10:
            return "X"
        elif card == 11:
            return "J"
        elif card == 12:
            return "Q"
        elif card == 13:
            return "K"
        elif card == 14:
            return "A"
    else:
        return str(card)

def hand_to_string(hand: list[int])-> str:
    """
    Changes a list of integers into their respective card names.

    Args:
    hand (list) - the list of hands.
    Returns a string with the correct hands.
    """
    return convert_hand(hand[0]) + " " + convert_hand(hand[1]) + " " + convert_hand(hand[2])

assert_equal(hand_to_string([4, 2, 3]), "4 2 3")
assert_equal(hand_to_string([4, 2, 10]), "4 2 X")
assert_equal(hand_to_string([12, 13, 14]), "Q K A")




def sort_hand(hand: list[int])-> list[int]:
    """
    Takes a list of three integers and sorts them from largest to smallest

    Args: hand (list) - The list of integers to be sorted

    Returns a list of intgers sorted from greatest to least
    """
    sort = hand
    # A simple Bubble sort algorithm
    for decrement in range(len(sort) - 1, 0, -1):
        for i in range(decrement):
            if sort[i] < sort[i+1]:
                swap = sort[i]
                sort[i] = sort[i+1]
                sort[i+1] = swap
    return sort

assert_equal(sort_hand([10, 12, 13]), [13, 12, 10])
assert_equal(sort_hand([1, 2, 3]), [3, 2, 1])
assert_equal(sort_hand([4, 3, 2]), [4, 3, 2])
assert_equal(sort_hand([1, 2, 3]), [3, 2, 1])






def has_triple(hand: list[int]) -> bool:
    """
    Accepts a list of integers and checks to see if they are identical

    Args:
    hand (list) - a list of integers

    Returns a boolean stating if it is identical or not
    """
    return hand[0] == hand[1] == hand[2]

assert_equal(has_triple([1, 1, 1]), True)
assert_equal(has_triple([2, 2, 2]), True)
assert_equal(has_triple([1, 2, 3]), False)





def has_straight(hand:list[int])-> bool:
    """
    Takes in a list of integers are returns whether the list is in direct consecutive order

    Args:
    hand (integer) - a list of integers sorted from greatest to least

    Returns whether the list is in direct consectuive order
    """
    return hand[1] == hand[0] - 1 and hand[2] == hand[1] - 1

assert_equal(has_straight([3, 2, 1]), True)
assert_equal(has_straight([5, 3, 2]), False)
assert_equal(has_straight([1, 2, 3]), False)





def has_pair(hand: list[int]) -> bool:
    """
    Takes in a list of integers and returns whether the list contains two identical numbers.

    Args:
    hand (integer): a list of integers sorted from greatest to least

    Retuns whether the list contains two identical numbers
    """
    return hand[0] == hand[1] or hand[1] == hand[2] or hand[0] == hand[2]

assert_equal(has_pair([1, 1, 2]), True)
assert_equal(has_pair([1, 1, 1]), True)
assert_equal(has_pair([1, 2, 3]), False)





def score_hand(hand: list[int]) -> int:
    """
    Takes in a list of strings and returns the value of the hand.

    Args:
    hand (intger) - a list of strings ordered from greatest to least

    Returns an integer that represents the value of the hand.
    """

    feature = 0

    if has_triple(hand):
        feature = 16

    # Must check for triple before the pair
    elif has_pair(hand):
        if hand[0] == hand[1]:
            feature = hand[0]
        elif hand[1] == hand[2]:
            feature = hand[1]
        else:
            feature = hand[0]

    elif has_straight(hand):
        feature = 15

    else:
        feature = 0

    return (feature * (16 ** 3)) + (hand[0] * (16 ** 2)) + (hand[1] * 16) + (hand[2])

assert_equal(score_hand([7, 4, 4]), 18244)
assert_equal(score_hand([11, 10, 9]), 64425)
assert_equal(score_hand([3, 3, 3]), 66355)





def dealer_plays(hand: list[int]) -> bool:
    """
    Takes in a list of integers and checks to see whether it satifies the playing conditions.

    Args:
    hand (integer) a list of integers ordered greatest to least

    Returns whether or not the hand has a queen high or better
    """

    return (hand[0] >= 12 or hand[1] >= 12 or hand[2] >= 12) or score_hand(hand) > 3803 # This is the highest score possible without a feature

assert_equal(dealer_plays([3, 2, 1]), True)
assert_equal(dealer_plays([4, 2, 1]), False)
assert_equal(dealer_plays([14, 14, 14]), True)
print("\n\n")




def play_round() -> int:
    """
    The main function of the program that returns whether the player won or lost the round.

    Returns the number of points the player gained or lost
    """
    phand = deal()
    print(hand_to_string(phand))

    if get_choice() == 'p':
        dhand = deal()
        print(hand_to_string(dhand))

        if dealer_plays(dhand):
            if score_hand(phand) > score_hand(dhand):
                return 20
            else:
                return -20
        else:
            return 10
    else:
        return -10


def get_choice() -> str:
    """
    Get user input and return either 'p' or 'f' depending on the player's choice.
    """
    answer= ' '
    while answer not in 'pf':
        answer=input("Please enter either 'p' or 'f':")
    return answer

from random import randint

def deal() -> list[int]:
    """
    Simple random card dealing function that returns three randomly chosen cards,
    represented as integers between 2 and 14.
    """
    return [randint(2, 14), randint(2, 14), randint(2, 14)]

score = 0
while True:
    score += play_round()
    print("Your score is", score, "- Starting a new round!")


def get_choice() -> str:
    """
    Get user input and return either 'p' or 'f' depending on the player's choice.
    """
    answer= ' '
    while answer not in 'pf':
        answer=input("Please enter either 'p' or 'f':")
    return answer

def deal() -> list[int]:
    """
    Simple random card dealing function that returns three randomly chosen cards,
    represented as integers between 2 and 14.
    """
    return [randint(2, 14), randint(2, 14), randint(2, 14)]

score = 0
while True:
    score += play_round()
    print("Your score is", score, "- Starting a new round!")
import random
from game_check import is_diablo_2_key, test_number_count
from validation import checksum
from util import get_mapping, print_key
import re

ALPHABET = "246789BCDEFGHJKMNPRTVWXZ"

def calculate_positions(target):
    """
    Calculates the positions of overflows required to 
    match our validation byte
    """

    binaryValue = bin(target)[2:]

    rotatedBinValue = binaryValue[::-1]

    positions = []
    for i, b in enumerate(rotatedBinValue):
        if b == '1':
            positions.append(i)

    return positions

def gen_random_value():
    """
    Generates us a 16 character starting value
    """
    # Need to take 9 values from the list and mix them into the output
    checkSumValues = ['0', '1', '2', '3', '4', '5', '6', '7']

    # First list half (x5 chars)
    firstHalf = []
    for x in range(2):
        firstHalf.append(random.choice(checkSumValues))

    for x in range(3):
        firstHalf.append(hex(random.randint(8, 15))[2:])

    lastHalf = []

    # Hacked values will give us 06 or 07
    lastHalf.append('3')
    lastHalf.append(random.choice(['3', '2']))

    # Last half x9 chars
    for x in range(5):
        lastHalf.append(random.choice(checkSumValues))

    for x in range(4):
        lastHalf.append(hex(random.randint(8, 15))[2:])

    output = "".join(firstHalf + lastHalf)

    assert(len(output) == 16)
    assert(test_number_count(output) == 9)

    return re.findall("..", output)

def get_key(value, positions):
    """
    This method takes an intermediate value (value) and finds what 
    letters give exactly the checksum value while having no pairs 
    that exceed 0xff in their (Validation value 0x00)

    Once we have this value we can select the pairs to 'overflow' 
    these change the result of the overflow validation but keeps the checksum
    exactly the same!
    """

    output = ""

    for i, v in enumerate(value):

        hVal = int(v, 16)

        if i in positions:
            hVal += 0x100

        for a in ALPHABET:
            for b in ALPHABET:

                temp = get_mapping(b) + get_mapping(a) * 0x18

                if hVal == temp:
                    output += a + b
                    break

    assert(len(output) == 16)

    return output

while True:
    rndValue = gen_random_value()
    target = checksum("".join(rndValue)) & 0xff
    positions = calculate_positions(target)

    key = get_key(rndValue, positions)

    if is_diablo_2_key(key):
        print_key(key)
    else:
        print("Invalid key generated!")

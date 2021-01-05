import re
import time
import string
import random

## Helper functions
def littleEndianFlip(value):
    parts = re.findall("..", value)
    return "".join(parts[::-1])

def gen_start(len=13):
    alphabet = string.ascii_uppercase + string.digits

    output = ""
    for x in range(len):
        output += random.choice(alphabet)

    return output

def print_key(string):
    parts = re.findall(".{4}", string)
    print("-".join(parts))
##

def transpose_00407b30(key):
    """
    The transposition operation performed by the program
    """

    ORDER = [0, 18, 13, 19, 14, 15, 6, 16, 8, 9, 10, 11, 17, 2, 4, 5, 7, 12, 1, 3]

    output = [""] * len(key)
    
    for i, o in enumerate(ORDER):
        output[o] = key[i]

    return "".join(output)

def tally_00407870(key):
    """
    Creates a integer from a key

    N.B Same as LOTR
    """

    charCount = 1
    doubleCount = 0
    for k in key:
        charCount += ord(k) % 0xfff1
        doubleCount += charCount % 0xfff1

    return (doubleCount * 0x10000 + charCount)

def shift1_00407990(seed):
    """
    Shifts around the values and produces a 
    7 character string

    N.B: Same as LOTR
    """

    VALUE = "64382957JKLMNPQRSTUVWXYZABCDEFGH"

    index = [0] * 7

    index[6] = seed & 0x1f
    index[5] = (seed >> 5) & 0x1f
    index[4] = (seed >> 10) & 0x1f
    index[3] = (seed >> 15) & 0x1f
    index[2] = (seed >> 20) & 0x1f
    index[1] = (seed >> 25) & 0x1f
    index[0] = index[0] | (index[6] & 7) << 2

    shifted_value = ""

    for x in index:
        shifted_value += VALUE[x]

    return shifted_value

def update_seed_00407950(key, seed, data):
    """
    Updates the seed using the updated key

    N.B: Same as LOTR
    """

    for k in key:

        startIndex = (ord(k) ^ seed) & 0xff
        startIndex *= 4

        data_hex = "".join(data[startIndex:startIndex + 4])
        data_value = int(littleEndianFlip(data_hex), 16)

        seed = (seed >> 8) ^ data_value

    return seed

def shift2_00407a60(param):
    VALUE = "23456789ABCDEFGHJKLMNPQRSTUVWXYZ"

    index = [0] * 7

    index[5] = (param >> 2) & 0x1f
    index[4] = (param >> 7) & 0x1f
    index[3] = (param >> 0xc) & 0x1f
    index[2] = (param >> 0x11) & 0x1f
    index[1] = (param >> 0x16) & 0x1f
    index[0] = (param >> 0x1b) & 0x1f

    #index[6] = (param & 3) << 3
    index[6] = (param & 3) * 8
    
    index[6] = index[6] | index[0] & 7

    shifted_value = ""

    for x in index:
        shifted_value += VALUE[x]

    return shifted_value

def validate(key):

    assert(len(key) == 20)

    t_key = transpose_00407b30(key)
    t = tally_00407870(t_key[:13])

    s1 = shift1_00407990(t ^ SEED)

    intermediate_key_1 = t_key[:13] + s1
    updated_seed = update_seed_00407950(intermediate_key_1, SEED, BIG_ARRAY)

    s2 = shift2_00407a60(updated_seed)

    final_key = transpose_00407b30(t_key[:13] + s2)

    return final_key

def keygen():

    while True:
        prefix = transpose_00407b30(gen_start() + "0000000")
        actual_key = validate(prefix)
        print_key(actual_key)

        time.sleep(0.01)

if __name__ == "__main__":
    SEED = 0x067F6B

    # Loads in the static memory
    with open("data.txt") as f:
        BIG_ARRAY = f.read().split(" ")

    keygen()


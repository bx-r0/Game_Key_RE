import re
import itertools
import string
import random
import time

## Helper methods
def littleEndianFlip(value):
    parts = re.findall("..", value)
    return "".join(parts[::-1])

def gen_start(len=13):
    SET = string.ascii_uppercase + string.digits

    output = ""
    for x in range(len):
        output += random.choice(SET)

    return output

def print_key(string):
    parts = re.findall(".{4}", string)
    print("-".join(parts))
##

def transpose(param):
    """
    The transposition operation performed by the program
    """

    ORDER = [0, 18, 13, 19, 14, 15, 6, 16, 8, 9, 10, 11, 17, 2, 4, 5, 7, 12, 1, 3]

    output = [""] * len(param)
    
    for i, o in enumerate(ORDER):
        output[o] = param[i]

    return "".join(output)

def function_0x405780_tally(param):

    charCount = 1
    doubleCount = 0
    for p in param:
        charCount += ord(p) % 0xfff1
        doubleCount += charCount % 0xfff1

    return (doubleCount * 0x10000 + charCount)

def function_0x405850_shift_1(param):
    
    VALUE = "64382957JKLMNPQRSTUVWXYZABCDEFGH"

    index = [0] * 7

    index[6] = param & 0x1f
    index[5] = (param >> 5) & 0x1f
    index[4] = (param >> 10) & 0x1f
    index[3] = (param >> 15) & 0x1f
    index[2] = (param >> 20) & 0x1f
    index[1] = (param >> 25) & 0x1f
    index[0] = index[0] | (index[6] & 7) << 2

    shifted_value = ""

    for x in index:
        shifted_value += VALUE[x]

    return shifted_value

def function_0x405910_shift_2(param):
    VALUE = "23456789ABCDEFGHJKLMNPQRSTUVWXYZ"

    index = [0] * 7

    index[5] = (param >> 2) & 0x1f
    index[4] = (param >> 7) & 0x1f
    index[3] = (param >> 0xc) & 0x1f
    index[2] = (param >> 0x11) & 0x1f
    index[1] = (param >> 0x16) & 0x1f
    index[0] = (param >> 0x1b) & 0x1f

    index[6] = (param & 3) << 3
    index[6] = index[6] | index[0] & 7

    shifted_value = ""

    for x in index:
        shifted_value += VALUE[x]

    return shifted_value

def function_fiddle_with_seed(transInput, seed):
    """
    Takes each value of the working key and mixes it with the 
    magic value (seed?)
    """

    for t in transInput:

        startIndex = (ord(t) ^ seed) & 0xff
        startIndex *= 4

        BIG_ARRAY_VALUE_HEX = "".join(BIG_ARRAY[startIndex:startIndex + 4])
        BIG_ARRAY_VALUE_HEX = littleEndianFlip(BIG_ARRAY_VALUE_HEX)
        BIG_ARRAY_VALUE = int(BIG_ARRAY_VALUE_HEX, 16)

        seed = (seed >> 8) ^ BIG_ARRAY_VALUE

    return seed

def validate(key):
    trans = transpose(key)
    tally = function_0x405780_tally(trans[:13])
    tally_xor = tally ^ SEED

    shifted = function_0x405850_shift_1(tally_xor)

    WORKING_STR = trans[:13] + shifted
    updated_seed = function_fiddle_with_seed(WORKING_STR, SEED)

    shifted2 = function_0x405910_shift_2(updated_seed)

    WORKING_STR = trans[:len(trans) - 7] + shifted2
    post_tranpose = transpose(WORKING_STR)

    # Returns isValid boolean and the expected end results
    return post_tranpose == key, shifted2

def gen_new_key():
    """
    This function works by placing a random 13 character prefix into the algorithm. This will define the
    values used for the seed and the randomness used. The algorithm will then create 7 characters from some binary operations on
    the first 13, if the output matches the last 7 characters of the input we have a valid key!

    Therefore, if we place in 13 values and 7 zeros (pre transposed to stop the program from muddling up the order) the program will fiddle with the
    values and return us the 7 characters it expects, if we extract this and place this onto the end of a new key we can 
    generate a valid key!
    """

    start_value = gen_start()

    input_value = transpose(start_value + "0000000")

    _, finalShiftedValue = validate(input_value)

    newKey = transpose(start_value + finalShiftedValue)

    validKey, _ =  validate(newKey)

    if validKey:
        print_key(newKey)
    else:
        Exception("Invalid key! We have a problem")

def keygen():

    while True:
        gen_new_key()
        time.sleep(0.1)

if __name__ == "__main__":
    SEED = 0x01D31C

    # Loads in the static memory
    with open("data.txt") as f:
        BIG_ARRAY = f.read().split(" ")

    keygen()
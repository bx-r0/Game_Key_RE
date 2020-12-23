import random

KEY = "3723630715868"

def valid_key(key):
    tally = 3

    # chr needs be in the range ('/' < X < ':')
    for i, k in enumerate(key):

        tally = tally + (tally * 2 ^ int(k))

        if (i + 1) > 11:

            # Checks the last value of the tally
            # if that matches 
            if key[12] == str(tally % 10):
                return True
                break

    else:
        return False

def gen_start():
    alphabet = list('0123456789')

    output = ""
    for x in range(12):
        output += random.choice(alphabet)

    return output

def calculate_tally(key):
    tally = 3
    for k in key:

        tally = tally + (tally * 2 ^ int(k))

    return str(tally % 10)

def print_key(key):

    pos = [4, 10]

    for p in pos:
        key = f"{key[:p]}-{key[p:]}"

    print(key)

def create_key():
    start = gen_start()
    checksum = calculate_tally(start)

    key = start + checksum

    valid = valid_key(key)

    if not valid:
        print("We have a problem! Invalid key found")
        exit()

    print_key(key)

valid_key(KEY)

while True:
    create_key()
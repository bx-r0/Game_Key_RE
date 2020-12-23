import rstr

def FUN_100015f0(key):
    """
    Function generates some sort of checksum for the input of a 
    16 character key
    """
    assert(len(key) == 16)

    checksum = 0xffffffff

    for i in range(16):
        index = (checksum ^ ord(key[i])) & 0xff
        checksum = int(BIG_ARRAY[index], 16) ^ (checksum >> 8)

    return checksum ^ 0xffffffff

def XOR_each_byte(cs):
    """
    Function uses some bitwise magic to XOR each byte together 

    BB04570B -> 0xBB ^ 0x04 ^ 0x57 ^ 0x0B
    """
    return cs & 0xff ^ (cs & 0xff00) >> 8 ^ (cs & 0xff0000) >> 0x10 ^ cs >> 0x18;

def validate_key(key):
    assert(len(key) == 18)

    actual_target_byte = int(key[-2:], 16)
    actual_key = key[:-2]

    checksum = FUN_100015f0(actual_key)

    target_byte = XOR_each_byte(checksum)

    if actual_target_byte == target_byte:
        print("Valid Key!")
    else:
        print("Invalid Key!")

def keygen(key_start=None):

    if key_start == None:
        key_start = rstr.xeger(r"([A-Z]|[0-9]){16}")

    checksum = FUN_100015f0(key_start)
    target_byte = XOR_each_byte(checksum)

    print(key_start + hex(target_byte)[2:].zfill(2).upper())


if __name__ == "__main__":
    # Loads big array of memory
    with open("values.txt") as f:
        BIG_ARRAY = f.readlines()

    BIG_ARRAY = list(map(str.strip, BIG_ARRAY))

    while True:
        keygen()

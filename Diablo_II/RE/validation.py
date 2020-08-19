import random
from util import get_mapping

# 42G2-MG6B-DHEE-RBR6

ALPHABET = "246789BCDEFGHJKMNPRTVWXZbcdefghjkmnprtvwxz"


def alpha_check(key):
    """
    Checks if a key contains the correct characters
    """

    for k in key:
        if not k in ALPHABET:
            return False

    return True

def createKeyHash(key):
    """
    The verification byte seems to be a flag for the pair combinations
    that when placed in the equation `var4 = var2 + var1 * 0x18` creates 
    a value higher than 0xff
    """

    key = list(key)

    verification_byte = 0x00

    var3 = 1
    i = 1
    while True:

        var1 = get_mapping(key[i - 1])
        var2 = get_mapping(key[i])

        var4 = var2 + var1 * 0x18

        if (0xff < var4):
            var4 -= 0x100

            # 0x191430
            verification_byte |= var3

        # Takes the hex value and spreads it across
        # to characters
        key[i - 1] = hex((var4 >> 4))[2:]
        key[i] = hex((var4 & 0xf))[2:]

        i += 2
        var3 = var3 << 1

        if (i > 0x10):
            break

        
    hashValue = "".join(key)

    return verification_byte, hashValue.upper()

def checksum(key):
    
    cs = 3

    for k in key:
        cs = cs + (int(k, 16) ^ cs * 2)

    return cs

def validate_key(key):

    if not alpha_check(key):
        print("Invalid characters in the key!")
        return False

    verification_byte, hashedKey = createKeyHash(list(key))

    cs = checksum(hashedKey)

    return (cs & 0xff) == verification_byte
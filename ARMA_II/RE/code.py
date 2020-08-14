import re
import os

def split_into_bytes(arr):
    return re.findall(r".{2}", arr)

def print_key(key):

    print(key[:4].upper(), end="-")

    parts = re.findall(r".{5}", key[4:])

    for p in parts[:-1]:
        print(p.upper(), end="-")

    print(parts[-1].upper())

def gen_key_base():
    
    res = ""
    for x in range(12):

        if x != 8:
            res += os.urandom(1).hex()
        else:
            res += "__"

    return res

def func_004022E0(key):
    STR = "0123456789ABCDEFGHJKLMNPRSTVWXYZ"

    assert(len(key) == 24)

    res = []

    blocks = re.findall(r".{8}", key)

    for block in blocks:

        total = 0
        shift_value = 0
        for b in block:
            i = STR.index(b.upper())

            shift = i << shift_value
            total |= shift

            shift_value += 5

        res.append(hex(total)[2:].zfill(10))
    return "".join(res)

def func_00416550(arr):
    
    total = 0

    arr_bytes = split_into_bytes(arr)

    value = 0
    for i, a in enumerate(arr_bytes[:-1]):

        for i in range(8 ):
            value = total >> 1

            if (total ^ (int(a, 16) >> i)) & 1 != 0:
                value ^= 0x8c   

            total = value

    return total

def check_key(key):

    # print(f"KEY: {key}")

    MEMORY = func_004022E0(key)
    assert len(MEMORY) == 30

    checkByte = func_00416550(MEMORY)

    MEMORY_bytes = split_into_bytes(MEMORY)

    # print(f"\tActual: \t{hex(checkByte)[2:].zfill(2)}")
    # print(f"\tExpecting: \t{MEMORY_bytes[-1]}")

    if hex(checkByte)[2:].zfill(2) == MEMORY_bytes[-1]:
        return True
    else:
        return False

while True:

    key_base = gen_key_base()

    for x in range(256):
        key = key_base.replace("__", hex(x)[2:].zfill(2))

        r = check_key(key)

        if r:
            print_key(key)
            break
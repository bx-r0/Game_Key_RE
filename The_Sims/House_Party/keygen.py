import rstr

def round(KEY, local_number8, local_number5, mod):

    key_len = len(KEY)

    local_number1 = 0

    while local_number5 < key_len:

        # This code makes a value with
        # the number of zeros of local_number8
        # i.e.
        #   > 5 = 10000
        local_number7 = 10 ** (local_number8 - 1)

        # Caps the value of "local_number11" to the key length
        temp = local_number5 + local_number8
        local_number11 = min(temp, key_len)

        local_number6 = local_number5

        while local_number6 < local_number11:

            if local_number6 >= 0:
                val = int(KEY[local_number6])
                local_number1 += val * local_number7
            
            local_number7 /= 10
            local_number6 += 1

        local_number1 = local_number1 % mod
        local_number5 += local_number8

    return int(local_number1)    

def function_20(KEY):
    assert(len(KEY) == 18)

    # Both rounds create each half of the four digit value
    r1 = round(KEY, 7, -5, 73)
    r2 = round(KEY, 5, 0, 79)

    return str(r1).zfill(2) + str(r2).zfill(2)

def validate(key):
    """
    Validates a provided key
    """
    assert(len(key) == 22)

    start = key[:18]
    end = key[18:]

    if key == "0000000000000000000000":
        return False

    actual = function_20(start)
    
    if actual != end:
        return False
    else:
        return True

def pretty_print_key(key):
    k = key[:4] + "-" + key[4:11] + "-" + key[11:18] + "-" + key[18:]
    print(k)

def keygen():
    """
    Generates a single valid key
    """
    
    start = rstr.xeger(r"([0-9]){18}")
    end = function_20(start)

    pretty_print_key(start + end)

    return start + end

if __name__ == "__main__":

    while True:
        valid = validate(keygen())

        if not valid:
            raise Exception("Invalid key generated!")


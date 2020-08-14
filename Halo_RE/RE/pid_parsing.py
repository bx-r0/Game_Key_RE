# Has already be shifted right once
VALIDATION_RESULT = 0x2322ea7

gudCode = "75043-036-8431757-40835"
badCode = "75043-2147-4836473-00339"


def gen_middle_section(validRes):

    # Cuts the value down to 6 digits
    value = validRes % 1000000

    digitTally = 0
    valueCopy = value
    if (value != 0):

        while True:
            remaining = int(valueCopy / 10)
            digitTally = digitTally + (valueCopy % 10)
            valueCopy = remaining

            if (remaining == 0): break

    # Appends a new value to the end
    return (value * 10 - digitTally % 7) + 7


def parseCode(code):

    parts = code.split("-")
    middle = parts[1] + parts[2][:-1]

    end = parts[3]

    binkVer = end[:2]
    tickCount = end[2:]

    print("=" * 50)
    print("CODE:", code)
    print()
    print("GAME ID:", hex(int(parts[0])))
    print("VALIDATION CODE:", hex(int(middle)))
    print("BINK VERSION:", hex(int(binkVer) << 1))
    print("TICK COUNT:", hex(int(tickCount)))
    print()
    print("=" * 50)
    print()

parseCode(gudCode)
parseCode(badCode)
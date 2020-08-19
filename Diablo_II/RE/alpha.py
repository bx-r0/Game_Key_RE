BIG_ARRY = [
    "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF",
    "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF",
    "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF",
    "FF", "FF", "00", "FF", "01", "FF", "02", "03", "04", "05", "FF", "FF", "FF", "FF", "FF", "FF",
    "FF", "FF", "06", "07", "08", "09", "0A", "0B", "0C", "FF", "0D", "0E", "FF", "0F", "10", "FF",
    "11", "FF", "12", "FF", "13", "FF", "14", "15", "16", "FF", "17", "FF", "FF", "FF", "FF", "FF",
    "FF", "FF", "06", "07", "08", "09", "0A", "0B", "0C", "FF", "0D", "0E", "FF", "0F", "10", "FF",
    "11", "FF", "12", "FF", "13", "FF", "14", "15", "16", "FF", "17", "FF", "FF", "FF", "FF", "FF",
    "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF",
    "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF",
    "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF",
    "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF",
    "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF",
    "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF",
    "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF",
    "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF", "FF"
]


def get_value(chr):
    return BIG_ARRY[ord(chr)]

for x in range(255):
    v = get_value(chr(x))

    if not v == "FF":
        print(chr(x), end="")

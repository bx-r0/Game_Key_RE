import re

MAPPING = {
    "2": "0",  "4": "1",  "6": "2",  "7": "3",  "8": "4",  "9": "5",
    "B": "6",  "C": "7",  "D": "8",  "E": "9",  "F": "10", "G": "11",
    "H": "12", "J": "13", "K": "14", "M": "15", "N": "16", "P": "17",
    "R": "18", "T": "19", "V": "20", "W": "21", "X": "22", "Z": "23",
    "b": "6",  "c": "7",  "d": "8",  "e": "9",  "f": "10", "g": "11",
    "h": "12", "j": "13", "k": "14", "m": "15", "n": "16", "p": "17",
    "r": "18", "t": "19", "v": "20", "w": "21", "x": "22", "z": "23"
}

def get_mapping(key):
    """
    Returns a value from the mapping dictionary
    """
    return int(MAPPING[key])

def print_key(key):

    parts = re.findall(".{4}", key)
    print("-".join(parts))

    
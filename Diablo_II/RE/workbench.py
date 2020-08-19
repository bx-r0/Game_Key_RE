import re

x = "010011101011001001011101000001"

values = re.findall(".{3}", x)

for v in values[::-1]: 
    print(int(v, 2), end=", ")
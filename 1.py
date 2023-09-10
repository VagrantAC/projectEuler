import math

multiple3 = math.ceil(1000 / 3)
multiple5 = math.ceil(1000 / 5)
multiple15 = math.ceil(1000 / 15)

res = (
    multiple3 * (multiple3 - 1) / 2 * 3
    + multiple5 * (multiple5 - 1) / 2 * 5
    - multiple15 * (multiple15 - 1) / 2 * 15
)

print(res)

import cmath

def get_res(name: str) -> int:
    res = 0
    for s in name:
        if s >= 'A' and s <= 'Z':
            res += ord(s) - ord('A') + 1
    return res


file = open('./0022_names.txt', 'r')
names = file.read().split(',')
names.sort()

res = 0
for i in range(0, len(names)):
    res += get_res(names[i]) * (i+1)

print(res)
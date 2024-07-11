
from math import sqrt


def is_abundant(num: int) -> int:
    res = 0
    for i in range(1, int(sqrt(num)+1)):
        if num % i == 0:
            res += i
            if i != num/i:
                res += num/i;
    return res - num

mp = {}
ls = []
n = 28124
for i in range(1, n):
    if is_abundant(i) > i:
        ls.append(i)

res = 0
print(len(ls))
for i in ls:
    for j in ls:
        if i+j >= n:
            continue
        mp[i+j] = True

for num in mp.keys():
    print(num)
    res += num
print((n - 1) * n / 2 - res)
from math import sqrt

def d(n: int) -> int:
    res = 0
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            res += i
            if n != i*i:
                res += n/i
    return int(res-n)
print(d(9))
cnt = 0
for i in range(1, 10001):
    res = d(i)
    if res > i and d(res) == i:
        cnt += res + i
        print(i, res)

print(cnt)
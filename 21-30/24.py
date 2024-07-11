n = 1000000 - 1
m = 10
# n = 0
# m = 3
fact = [1]
for i in range(1, m):
    fact.append(fact[-1] * i)

mp = {}
for i in range(0, m):
    res = int(n / fact[m-i-1])
    n %= fact[m-i-1]
    # print(n, "===", res, "===", fact[m-i-1])
    for j in range(0, m):
        if res == 0 and mp.get(j) is None:
            mp[j] = True
            print(j, end='')
            break
        if mp.get(j) is None:
            res -= 1
n = 20
k = n

vis = {}
primes = []
for i in range(2, k):
    if vis.get(i) is None:
        vis[i] = True
        primes.append(i)
    for prime in primes:
        if i * prime > k:
            break
        vis[i * prime] = False

cnts = {}
for i in range(1, n):
    tmp = i
    for prime in primes:
        cnt = 0
        while tmp % prime == 0:
            tmp /= prime
            cnt += 1
        cnts[prime] = max(cnts.get(prime, 0), cnt)

res = 1
for key in cnts.keys():
    for i in range(0, cnts.get(key, 0)):
        res = res * key

print(res)

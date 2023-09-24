n = 2000000
vis = {}
primes = []

for i in range(2, n):
    if vis.get(i) is None:
        primes.append(i)

    for prime in primes:
        if i * prime > n:
            break
        vis[i * prime] = False
        if i % prime == 0:
            break

res = 0
for prime in primes:
    res += prime
print(res)

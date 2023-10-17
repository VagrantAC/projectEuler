n = 1000000
vis = {}
primes = []

for i in range(2, n):
    if vis.get(i) is None:
        vis[i] = True
        primes.append(i)
    for prime in primes:
        if i * prime > n:
            break
        vis[i * prime] = False
        if i % (prime) == 0:
            break

print(primes[10000])

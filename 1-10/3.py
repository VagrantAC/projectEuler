import math

vis = {}
primes = []
n = 600851475143
k = int(math.sqrt(n))
for i in range(2, k):
    if vis.get(i) is None:
        vis[i] = True
        primes.append(i)
    for prime in primes:
        if i * prime > k:
            break
        vis[i * prime] = False

primes.reverse()
for prime in primes:
    if n % prime == 0:
        print(prime)
        break

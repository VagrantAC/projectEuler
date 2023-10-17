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

for i in range(1, n):
    num = int(i * (i+1) / 2)
    sum = 1
    for prime in primes:
        count = 1

        while int(num) % prime == 0:
            count += 1
            num /= prime
        sum *= count
        if int(num) == 1:
            break

    if sum > 500:
        print(i * (i+1)/2)
        break

f1, f2 = 0, 1
f3 = 1

res = 0
while f3 <= 4000000:
    f1 = f2
    f2 = f3
    f3 = f1 + f2

    if f3 % 2 == 0:
        res += f3

print(res)

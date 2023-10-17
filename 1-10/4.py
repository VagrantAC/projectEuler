res = 0
for i in range(1, 999):
    for j in range(1, 999):
        k = i * j
        if len(str(k)) == 6 and str(k)[::-1] == str(k):
            res = max(res, k)

print(res)

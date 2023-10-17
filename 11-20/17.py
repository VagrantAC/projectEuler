onesPlace = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
tensPlace = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]

res = 0
for i in [3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]:
    res += i

for i in range(2, 10):
    for j in range(0, 10):
        res += onesPlace[j] + tensPlace[i]

sum = res * 10
for i in range(1, 10):
    sum += onesPlace[i] * 100 + 990 + 7

print(sum + 11)

# One 3
# Two 3
# Three 5
# Four 4
# Five 4
# Six 3
# Seven 5
# Eight 5
# Nine 4
# Ten 3
# Eleven 6
# Twelve 6
# Thirteen 8
# Fourteen 8
# Fifteen 7
# Sixteen 7
# Seventeen 9
# Eighteen 8
# Nineteen 8
# Twenty 6

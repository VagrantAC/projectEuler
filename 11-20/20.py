def solve():
    res = 1
    for i in range(1, 101):
        res *= i
    print(res)
    return res


def getSum(num: int):
    res = 0
    for str in num.__str__():
        res += int(str)
    return res


print(getSum(solve()))

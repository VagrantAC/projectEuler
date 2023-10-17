def qpow(a: int, b: int):
    res = 1
    while b:
        if b & 1:
            res = res * a

        b = b >> 1
        a = a * a
    return res


def getSum(num: int):
    res = 0
    for n in num.__str__():
        res = res + int(n)
    return res


print(getSum(qpow(2, 1000)))

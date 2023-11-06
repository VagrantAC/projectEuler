months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def leapYear(year: int):
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0


def solve():
    ans = 0
    res = 0
    for year in range(1900, 2001):
        if leapYear(year):
            months[1] = 29
        else:
            months[1] = 28
        for month in months:
            ans += month
            ans %= 7
            if ans == 6 and year != 1900:
                res += 1
    return res


print(solve())

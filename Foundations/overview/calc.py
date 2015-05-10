import math
from decimal import *

sec = 1000000
minute = 60 * sec
hour = 60 * minute
day = 24 * hour
month = 30 * day
year = 365 * day
century = 100 * year

# n * lg(n) == c
# ==> 2 ** (lg(n)) * lg (n) == c
# ==> lg(n) == W(c)
# ==> n == exp(W(c))
# see http://en.wikipedia.org/wiki/Lambert_W_function#Example_2


def n_lgn(c):
    lower = 0.0
    upper = 10e13
    while True:
        middle = (lower + upper) / 2
        if lower == middle or middle == upper:
            return middle
        if middle * math.log(middle, 2) > c:
            upper = middle
        else:
            lower = middle


# n!
def de_factorial(c):
    n = 0
    while True:
        if math.factorial(n) >= c:
            return n - 1
        else:
            n += 1

# lg(n)
print("2 ^ 10 ^ 6")
print("2 ^ ( %d * 10 ^ 6 )" % (minute / sec))
print("2 ^ ( %d * 10 ^ 6 )" % (hour / sec))
print("2 ^ ( %d * 10 ^ 6 )" % (day / sec))
print("2 ^ ( %d * 10 ^ 6 )" % (month / sec))
print("2 ^ ( %d * 10 ^ 6 )" % (year / sec))
print("2 ^ ( %d * 10 ^ 6 )" % (century / sec))
print("")
# sqrt(n)
print("{:.1e}".format(Decimal(sec ** 2)))
print("{:.1e}".format(Decimal(minute ** 2)))
print("{:.3e}".format(Decimal(hour ** 2)))
print("{:.5e}".format(Decimal(day ** 2)))
print("{:.6e}".format(Decimal(month ** 2)))
print("{:.9e}".format(Decimal(year ** 2)))
print("{:.9e}".format(Decimal(century ** 2)))
print("")
# n
print("{:.1e}".format(Decimal(sec)))
print("{:.1e}".format(Decimal(minute)))
print("{:.1e}".format(Decimal(hour)))
print("{:.2e}".format(Decimal(day)))
print("{:.3e}".format(Decimal(month)))
print("{:.4e}".format(Decimal(year)))
print("{:.4e}".format(Decimal(century)))
print("")
# n lg(n)
print(n_lgn(sec))
print(n_lgn(minute))
print(n_lgn(hour))
print(n_lgn(day))
print(n_lgn(month))
print(n_lgn(year))
print(n_lgn(century))
print("")
# n^2
print(math.sqrt(sec))
print(math.sqrt(minute))
print(math.sqrt(hour))
print(math.sqrt(day))
print(math.sqrt(month))
print(math.sqrt(year))
print(math.sqrt(century))
print("")
# n^3
print(sec ** (1 / 3.0))
print(minute ** (1 / 3.0))
print(hour ** (1 / 3.0))
print(day ** (1 / 3.0))
print(month ** (1 / 3.0))
print(year ** (1 / 3.0))
print(century ** (1 / 3.0))
print("")
# 2^n
print(math.log(sec, 2))
print(math.log(minute, 2))
print(math.log(hour, 2))
print(math.log(day, 2))
print(math.log(month, 2))
print(math.log(year, 2))
print(math.log(century, 2))
print("")
# n!
print(de_factorial(sec))
print(de_factorial(minute))
print(de_factorial(hour))
print(de_factorial(day))
print(de_factorial(month))
print(de_factorial(year))
print(de_factorial(century))
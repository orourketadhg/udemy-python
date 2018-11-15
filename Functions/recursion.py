# generally recursion is not used in python
# can effects the processing time due to stacking


# factorial(n)
def fact(n):
    result = 1
    if n > 1:
        for f in range(1, n + 1):
            result *= f
    return result


for i in range(15):
    print(i, ': ', fact(i))


# factorial(n) using recursion
def fact_rec(n):
    if n <= 1:
        return 1
    else:
        return n * fact_rec(n - 1)


for i in range(15, 0, -1):
    print(i, ': ', fact_rec(i))

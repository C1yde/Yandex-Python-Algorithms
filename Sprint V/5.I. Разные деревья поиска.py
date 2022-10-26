def main():
    n = int(input())

    print(catalan(n))


def catalan(n):
    c = binomialCoeff(2 * n, n)
 
    return c // (n + 1)


def binomialCoeff(n, k):
    res = 1

    if (k > n - k):
        k = n - k
 
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
     
    return res


if __name__ == '__main__':
    main()

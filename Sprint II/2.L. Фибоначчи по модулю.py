import sys


def main():
    line = sys.stdin.readline().rstrip()
    n, k = line.split()
    n = int(n)
    k = int(k)

    print(get_last_digits(fib(n), k))

def fib(n):
    v1, v2, v3 = 1, 1, 0
    for rec in bin(n)[3:]:
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v1

def get_last_digits(sum, count):
    return sum % (10**count)

if __name__ == '__main__':
    main()

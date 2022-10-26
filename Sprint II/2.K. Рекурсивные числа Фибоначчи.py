def main():
    n = int(input())

    print(sum(n))

def sum(n):
    if n == 1 or n == 0:
        return 1
    return sum(n - 1) + sum(n - 2) 

if __name__ == '__main__':
    main()

import sys

def main():
    number = int(input())

    if number == 0:
        print(0)
        return
    
    result = []
    while number > 1:
        result.append(number % 2)
        number = number // 2

    result.append(1)
    result.reverse()
    print(*result, sep='')

if __name__ == '__main__':
    main()

def main():
    number = int(input())

    if number == 0:
        print(False)

    while number % 4 == 0:
        number = number / 4

    print(number == 1)

if __name__ == '__main__':
    main()

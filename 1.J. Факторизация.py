def main():
    number = int(input())

    result = []
    i = 2
    while i * i <= number:
        while number % i == 0:
            number = number // i
            result.append(i)
        else:
            i = i + 1

    if len(result) == 0:
        result.append(number)
    else:
        if number > 1:
            result.append(number)

    print(*result)

if __name__ == '__main__':
    main()

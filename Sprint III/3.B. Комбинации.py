import sys


def main():
    numbers = list(map(int, input()))

    arr = []
    for i in range(len(numbers)):
        arr.append(get_arr_of_symbols(numbers[i]))

    gen_string(arr, 0, '')


def gen_string(arr, array_index, prefix):
    if array_index == len(arr):
        print(prefix, end=' ')
        return

    for symbol in arr[array_index]:
        gen_string(arr, array_index + 1, prefix + symbol)


def get_arr_of_symbols(number):
    if number == 2:
        return ['a', 'b', 'c']
    elif number == 3:
        return ['d', 'e', 'f']
    elif number == 4:
        return ['g', 'h', 'i']
    elif number == 5:
        return ['j', 'k', 'l']
    elif number == 6:
        return ['m', 'n', 'o']
    elif number == 7:
        return ['p', 'q', 'r', 's']
    elif number == 8:
        return ['t', 'u', 'v']
    elif number == 9:
        return ['w', 'x', 'y', 'z']


if __name__ == '__main__':
    main()

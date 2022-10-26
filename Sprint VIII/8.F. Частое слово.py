import sys


def main():
    n = int(input())

    dict = {}
    for __ in range(n):
        word = sys.stdin.readline().rstrip()

        if word in dict:
            dict[word] += 1
        else:
            dict.setdefault(word, 1)

    sorted_dict = sorted(dict.items(), key=lambda item: (-item[1], item[0]))

    print(sorted_dict[0][0])


if __name__ == '__main__':
    main()

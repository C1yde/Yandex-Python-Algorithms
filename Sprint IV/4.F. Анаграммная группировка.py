import sys


def main():
    n = int(input())
    line = sys.stdin.readline().rstrip()
    words = line.split()

    dict = {}
    for i in range(len(words)):
        word = words[i]
        sorted_word = ''.join(sorted(word))
        if sorted_word in dict:
            dict[sorted_word].append(i)
        else:
            dict.setdefault(sorted_word, [i])
    
    values = list(dict.values())
    for group in sorted(values, key=lambda value: value[0]):
        print(*group)


if __name__ == '__main__':
    main()

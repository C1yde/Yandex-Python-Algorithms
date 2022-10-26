import sys

def main():
    length = int(input())
    line = sys.stdin.readline().rstrip()
    words = list(map(str, line.split()))

    longestWord = words[0]
    longestLength = len(longestWord)
    for word in words:
        wordLength = len(word)
        if wordLength > longestLength:
            longestWord = word
            longestLength = wordLength

    print(longestWord)
    print(longestLength)

if __name__ == '__main__':
    main()

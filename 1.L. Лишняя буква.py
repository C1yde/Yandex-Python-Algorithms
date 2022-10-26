import sys

def main():
    line = sys.stdin.readline().rstrip()
    s = list(map(str, line))
    line = sys.stdin.readline().rstrip()
    t = list(map(str, line))

    for i in range(0, len(t)):
        for j in range(0, len(s)):
            if s[j] == t[i]:
                s.remove(s[j])
                break
        else:
            print(t[i])
            return

if __name__ == '__main__':
    main()

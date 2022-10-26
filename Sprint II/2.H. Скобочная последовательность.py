import sys


def main():
    line = sys.stdin.readline().rstrip()

    if not line:
        print(True)
        return
    
    while '()' in line or '[]' in line or '{}' in line:
        line = line.replace('()', '')
        line = line.replace('[]', '')
        line = line.replace('{}', '')

    print(not line)


if __name__ == '__main__':
    main()

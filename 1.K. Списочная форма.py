import sys

def main():
    length = int(input())
    line = sys.stdin.readline().rstrip()
    form = int(''.join(map(str, line.split())))
    k = int(input())

    result = form + k
    
    result = [str(x) for x in str(result)]

    print(*result)

if __name__ == '__main__':
    main()

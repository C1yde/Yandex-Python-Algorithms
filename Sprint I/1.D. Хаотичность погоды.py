import sys

def main():
    period = int(input())
    line = sys.stdin.readline().rstrip()
    temperatures = list(map(int, line.split()))

    if period == 1:
        print(1)
        return

    result = 0
    if temperatures[0] > temperatures[1]:
        result += 1
    if temperatures[period - 1] > temperatures[period - 2]:
        result += 1

    for i in range(0, period - 1):
        if i == 0 or i == period - 1:
            continue
        if temperatures[i] > temperatures[i + 1] and temperatures[i] > temperatures[i - 1]:
            result += 1

    print(result)

if __name__ == '__main__':
    main()

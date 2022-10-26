import sys

def main():
    line = sys.stdin.readline().rstrip()
    first = list(map(int, line))
    line = sys.stdin.readline().rstrip()
    second = list(map(int, line))
    firstLength = len(first)
    secondLength = len(second)
    diff = 0

    if secondLength > firstLength:
        diff = secondLength - firstLength
        tmp = first
        first = second
        second = tmp
    else:
        diff = firstLength - secondLength

    result = getResult(first, second, diff)

    print(*result, sep='')

def getResult(first, second, diff):
    result = []
    add = False
    for i in range(len(first) - 1, -1, -1):
        j = i - diff
        secondValue = 0
        if j >= 0:
            secondValue = second[j]

        sum = first[i] + secondValue

        if add:
            sum += 1
            add = False

        if sum > 1:
            result.append(sum - 2)
            add = True
        else:
            result.append(sum)

    if add:
        result.append(1)

    result.reverse()
    return result

if __name__ == '__main__':
    main()

import sys


def main():
    n = int(input())
    line = sys.stdin.readline().rstrip()
    array = list(map(int, line.split()))
    k = int(input())

    counted_values = [0] * 10000
    for value in array:
        counted_values[value] += 1

    index = 0
    for i in range(10000):
        for amount in range(counted_values[i]):
            array[index] = i
            index += 1

    result = []
    previous_item = None
    for item in array:
        if previous_item is None or previous_item != item:
            result.append([item, 1])
            previous_item = item
        else:
            result[-1][1] += 1

    result.sort(key=lambda item: -item[1])

    for item in result[:k]:
        print(item[0], end=' ')

        
if __name__ == '__main__':
    main()

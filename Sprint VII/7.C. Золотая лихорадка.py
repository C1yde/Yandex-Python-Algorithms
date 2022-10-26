import sys
import heapq


def main():
    m = int(input())
    n = int(input())

    heap = []
    for __ in range(n):
        line = sys.stdin.readline().rstrip()
        values = list(map(int, line.split()))
        cost = values[0]
        weight = values[1]

        heapq.heappush(heap, (-cost, weight))

    total = 0
    while len(heap) > 0 and m > 0:
        values = heapq.heappop(heap)
        cost = -values[0]
        weight = values[1]
        
        if weight < m:
            total += cost * weight
        else:
            total += cost * m
        
        m -= weight
    
    print(total)


if __name__ == '__main__':
    main()

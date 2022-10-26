import sys
import heapq


def main():
    n = int(input())

    lessons = []
    for __ in range(n):
        line = sys.stdin.readline().rstrip()
        times = list(map(str, line.split()))
        start_time = parse_time(times[0])
        end_time = parse_time(times[1])

        heapq.heappush(lessons, (end_time, start_time))

    count = 0
    result = []
    last_end_time = None
    while len(lessons) > 0:
        lesson = heapq.heappop(lessons)

        if last_end_time is not None and lesson[1] < last_end_time :
            continue

        last_end_time = lesson[0]
        count += 1

        result.append(f"{lesson[1]} {lesson[0]}")
    
    print(count)
    print(*result, sep='\n')


def parse_time(time_string):
    if '.' in time_string:
        return float(time_string)

    return int(time_string)


if __name__ == '__main__':
    main()

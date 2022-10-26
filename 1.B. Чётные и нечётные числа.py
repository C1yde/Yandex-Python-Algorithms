import sys

def main():
    line = sys.stdin.readline().rstrip()
    x1, x2, x3 = line.split()
    x1 = int(x1)
    x2 = int(x2)
    x3 = int(x3)
    sum = 0
    for number in [x1, x2, x3]:
        sum += number % 2
    
    if sum == 0 or sum == 3:
        print("WIN")
    else:
        print("FAIL")

if __name__ == '__main__':
    main()

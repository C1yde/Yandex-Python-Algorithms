import sys


def main():
    n = int(input())
    gen_brackets(n, 0, 0, '')


def gen_brackets(n, open_count, close_count, prefix):
    if open_count + close_count == 2 * n:
        print(prefix)
        return
    
    if open_count < n:
        gen_brackets(n, open_count + 1, close_count, prefix + '(')
    if open_count > close_count:
        gen_brackets(n, open_count, close_count + 1, prefix + ')')


if __name__ == '__main__':
    main()

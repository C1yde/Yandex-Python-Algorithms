def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)

    s1, t1 = '', ''
    i = 0
    j = 0
    while i < n or j < m:
        if i < n:
            if ord(s[i]) % 2 == 0:
                s1 += s[i]
            i += 1

        if j < m:
            if ord(t[j]) % 2 == 0:
                t1 += t[j]
            j += 1

    if s1 == t1:
        print(0)
    elif s1 > t1:
        print(1)
    else:
        print(-1)


if __name__ == '__main__':
    main()

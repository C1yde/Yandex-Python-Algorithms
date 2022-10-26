import sys


def main():
    s = sys.stdin.readline().rstrip()
    t = sys.stdin.readline().rstrip()
    
    if len(s) < len(t):
        print('NO')
        return
        
    dict_s = {}
    dict_t = {}
    i = 0
    while i < len(s) and i < len(t):
        symbol_t = dict_s.get(s[i])
        if symbol_t is None:
            symbol_s = dict_t.get(t[i])
            if symbol_s is None:
                dict_t.setdefault(t[i], s[i])
            else:
                if symbol_s != s[i]:
                    print('NO')
                    return
            dict_s.setdefault(s[i], t[i])
        else:
            if symbol_t != t[i]:
                print('NO')
                return
        i += 1

    print('YES')


if __name__ == '__main__':
    main()

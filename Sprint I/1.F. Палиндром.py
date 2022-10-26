import sys

def main():
    frase = sys.stdin.readline().rstrip()
    fraseLength = len(frase)
    i = 0
    j = fraseLength - 1
    while i < j:
        if not frase[i].isalnum() or frase[i] == ' ':
            i += 1
            continue
        if not frase[j].isalnum() or frase[j] == ' ':
            j -= 1
            continue
        if frase[i].lower() != frase[j].lower():
            print(False)
            return
        i += 1
        j -= 1

    print(True)

if __name__ == '__main__':
    main()

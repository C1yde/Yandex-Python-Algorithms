import sys


def main():
    s = str(input())

    if len(s) == 1:
        print(1)
        return

    max_length = 0
    current_dict = {}
    i = 0
    while i < len(s):
        if s[i] not in current_dict:
            current_dict.setdefault(s[i], i)
            i += 1
        else:
            max_length = get_max(max_length, len(current_dict))
            previous_index = current_dict[s[i]]
            i = previous_index + 1
            current_dict.clear()

    max_length = get_max(max_length, len(current_dict))
    print(max_length)

def get_max(current_max, new_value):
    if new_value > current_max:
        return new_value
    return current_max

  
if __name__ == '__main__':
    main()

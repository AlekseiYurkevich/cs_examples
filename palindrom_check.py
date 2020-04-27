def is_palindrom(string):
    reverse_string = ""
    for i in reversed(range(len(string))):
        reverse_string += string[i]
    return string == reverse_string


def is_palindrom(string):
    reverse_string = []
    for i in reversed(range(len(string))):
        reverse_string.append(string[i])
    return string == "".join(reverse_string)


def is_palindrom(string):
    left_idx = 0
    right_idx = len(string) - 1

    while left_idx < right_idx:
        if string[left_idx] != string[right_idx]:
            return False
        left_idx += 1
        right_idx -= 1
    return True

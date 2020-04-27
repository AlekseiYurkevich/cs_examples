#  Implement a function to reverse a string (a list of characters), in-place.
# None -> None
# [''] -> ['']
# ['f', 'o', 'o', ' ', 'b', 'a', 'r'] -> ['r', 'a', 'b', ' ', 'o', 'o', 'f']

# Complexity:

# Time: O(n)
# Space: O(1)


def reverse_strings(string_value):
    if string_value is None:
        return string_value

    return string_value[::-1]


def reverse_strings_alt(string_value):
    if string_value is None or not isinstance(string_value, str):
        return string_value

    return "".join(reversed(string_value))


if __name__ == "__main__":
    print(string_value(["f", "b"]))


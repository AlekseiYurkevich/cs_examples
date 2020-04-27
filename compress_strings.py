# Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'. Only compress the string if it saves space.

# None -> None
# '' -> ''
# 'AABBCC' -> 'AABBCC'
# 'AAABCCDDDD' -> 'A3BC2D4'


def compress(stringvalue):
    if stringvalue is None or not isinstance(stringvalue, str):
        return stringvalue
    result = ""
    prev_char = stringvalue[0]
    count = 0
    for char in stringvalue:
        if char == prev_char:
            count += 1
        else:
            result += _calc_partial_result(prev_char, count)
            prev_char = char
            count = 1
    result += _calc_partial_result(prev_char, count)
    return result if len(result) < len(stringvalue) else stringvalue


def _calc_partial_result(prev_char, count):
    return prev_char + (str(count) if count > 1 else "")


if __name__ == "__main__":
    print(compress("AAABCCDDDDE"))
    print(compress(5))
    print(compress("AABBCC"))

def caesar_encrypt(string, key):
    # check test if needed
    new_letter = []
    new_key = key % 26
    alphabet = list("abcdefghigklmnopqrstuvwxyz")

    for letter in string:
        new_letter.append(get_new_letter(letter, new_key, alphabet))
    return "".join(new_letter)


def get_new_letter(letter, new_key, alphabet):
    new_letter_code = alphabet.index(letter) + new_key
    return (
        alphabet[new_letter_code]
        if new_letter_code <= 25
        else alphabet[-1 + new_letter_code % 25]
    )


if __name__ == "__main__":
    print(caesar_encrypt("xyz", 2))

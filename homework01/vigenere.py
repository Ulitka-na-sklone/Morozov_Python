def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """

    def shift(letter):
        if 97 <= ord(plaintext[i]) <= 122:
            return ord(letter) - 97
        elif 65 <= ord(plaintext[i]) <= 90:
            return ord(letter) - 65

    full_keyword = ""
    for i in range(len(plaintext)):
        while i >= len(keyword):
            i -= len(keyword)
        full_keyword += keyword[i]

    len_of_alphabet = 26
    ciphertext = ""
    for i in range(len(plaintext)):
        if 97 <= ord(plaintext[i]) <= 122:
            if 97 <= ord(plaintext[i]) + shift(full_keyword[i]) <= 122:
                ciphertext += chr(ord(plaintext[i]) + shift(full_keyword[i]))
            else:
                ciphertext += chr(ord(plaintext[i]) + shift(full_keyword[i]) - len_of_alphabet)
        elif 65 <= ord(plaintext[i]) <= 90:
            if 65 <= ord(plaintext[i]) + shift(full_keyword[i]) <= 90:
                ciphertext += chr(ord(plaintext[i]) + shift(full_keyword[i]))
            else:
                ciphertext += chr(ord(plaintext[i]) + shift(full_keyword[i]) - len_of_alphabet)
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """

    def shift(letter):
        if 97 <= ord(ciphertext[i]) <= 122:
            return ord(letter) - 97
        elif 65 <= ord(ciphertext[i]) <= 90:
            return ord(letter) - 65

    full_keyword = ""
    for i in range(len(ciphertext)):
        while i >= len(keyword):
            i -= len(keyword)
        full_keyword += keyword[i]

    len_of_alphabet = 26
    plaintext = ""

    for i in range(len(ciphertext)):
        if 97 <= ord(ciphertext[i]) <= 122:
            if 97 <= ord(ciphertext[i]) - shift(full_keyword[i]) <= 122:
                plaintext += chr(ord(ciphertext[i]) - shift(full_keyword[i]))
            else:
                plaintext += chr(ord(ciphertext[i]) - shift(full_keyword[i]) + len_of_alphabet)
        elif 65 <= ord(ciphertext[i]) <= 90:
            if 65 <= ord(ciphertext[i]) - shift(full_keyword[i]) <= 90:
                plaintext += chr(ord(ciphertext[i]) - shift(full_keyword[i]))
            else:
                plaintext += chr(ord(ciphertext[i]) - shift(full_keyword[i]) + len_of_alphabet)
        else:
            plaintext += ciphertext[i]
    return plaintext

import typing as tp

def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    len_of_alphabet = 26
    ciphertext = ""
    while shift > len_of_alphabet:
        shift -= len_of_alphabet
    for i in range(len(plaintext)):
        if 97 <= ord(plaintext[i]) <= 122:
            if 97 <= ord(plaintext[i]) + shift <= 122:
                ciphertext += chr(ord(plaintext[i]) + shift)
            else:
                ciphertext += chr(ord(plaintext[i]) + shift - len_of_alphabet)
        elif 65 <= ord(plaintext[i]) <= 90:
            if 65 <= ord(plaintext[i]) + shift <= 90:
                ciphertext += chr(ord(plaintext[i]) + shift)
            else:
                ciphertext += chr(ord(plaintext[i]) + shift - len_of_alphabet)
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    len_of_alphabet = 26
    plaintext = ""
    while shift > len_of_alphabet:
        shift -= len_of_alphabet
    for i in range(len(ciphertext)):
        if 97 <= ord(ciphertext[i]) <= 122:
            if 97 <= ord(ciphertext[i]) - shift <= 122:
                plaintext += chr(ord(ciphertext[i]) - shift)
            else:
                plaintext += chr(ord(ciphertext[i]) - shift + len_of_alphabet)
        elif 65 <= ord(ciphertext[i]) <= 90:
            if 65 <= ord(ciphertext[i]) - shift <= 90:
                plaintext += chr(ord(ciphertext[i]) - shift)
            else:
                plaintext += chr(ord(ciphertext[i]) - shift + len_of_alphabet)
        else:
            plaintext += ciphertext[i]
    return plaintext
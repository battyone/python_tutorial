from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    tb: bytes = token_bytes(length)

    # convert to bit string
    return int.from_bytes(tb, byteorder='big')


def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))

    original_key: int = int.from_bytes(original_bytes, byteorder='big')
    encrypted: int = original_key ^ dummy
    return dummy, encrypted


def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2
    temp: bytes = decrypted.to_bytes(
        (decrypted.bit_length() + 7) // 8, byteorder='big')

    return temp.decode()


s = 'Hello World! This is an encryption test.'
key1, key2 = encrypt(s)
t = decrypt(key1, key2)
print(key1, key2)
print(s == t)

from hashids import Hashids
from typing import Tuple

class Hashing:
    def __init__(self):
        self.hash = Hashids(salt='xm0oswy23h')

    def generate_hash_key(self, id: int) -> str:
        hashed = self.hash.encode(id)
        return hashed

    def decode_hash_key(self, key: str) -> Tuple[int, None]:
        unhashed = self.hash.decode(key)
        return unhashed
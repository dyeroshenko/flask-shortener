from hashids import Hashids

class Hashing:
    def __init__(self):
        self.hash = Hashids(salt='xm0oswy23h')

    def generate_hash_key(self, id):
        hashed = self.hash.encode(id)
        return hashed

    def decode_hash_key(self, key):
        unhashed = self.hash.decode(key)
        return unhashed
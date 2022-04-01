import hashlib

hash0 = bytes.fromhex('c117ea8ec828342f4dfb0ad6bd140e03a50720ece40169ee38b\
dc15d9eb64cf5')
hash1 = bytes.fromhex('c131474164b412e3406696da1ee20ab0fc9bf41c8f05fa8ceea\
7a08d672d7cc5')
parent = hashlib.sha256(hash0 + hash1)
print(parent)
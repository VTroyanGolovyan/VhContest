import hashlib

# local salt param
local_salt = 'VHcontest-the-best!'


def get_hash(password, salt):
    hash_str = password + salt + local_salt
    return hashlib.sha512(hash_str.encode('utf-8')).hexdigest()


def compareHashes(first, second):
    print(hashlib.sha512(first.encode('utf-8')).hexdigest())
    print(hashlib.sha512(second.encode('utf-8')).hexdigest())
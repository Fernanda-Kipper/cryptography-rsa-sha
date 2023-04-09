import itertools
import hashlib

def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return ''.join(lines)

def brute_force_decryptor(key_for_rsa_public):
    all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    unique_combinations = itertools.product(all_letters, repeat=10)
    for combination in unique_combinations:
        current_combination = 'an' + ''.join(combination)
        hash_object = hashlib.sha256()
        hash_object.update(current_combination.encode())
        hash_sha256 = hash_object.hexdigest()
        if(hash_sha256 == key_for_rsa_public):
            print('eureka')
            print(current_combination)
            break

key_for_rsa_public = read_file('key_for_rsa_public.hash')
brute_force_decryptor(key_for_rsa_public)
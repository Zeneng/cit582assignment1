
def encrypt(key,plaintext):
    M = [(ord(x) + key)% 26 + 65  for x in plaintext]
    S = [chr(x) for x in M]
    ciphertext=''.join(S)
    return ciphertext

def decrypt(key,ciphertext):
    M = [(ord(x) - key)% 26 + 65  for x in ciphertext]
    S = [chr(x) for x in M]
    plaintext = ''.join(S)
    return plaintext



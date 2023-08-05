import secrets
import string

def generate_token(ranged=20):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(ranged))
    return password

class Encryptor:
    def __init__(self, token):
        self.token = token
    
    def encrypt(self, text:str):
        token_solved = 0
        for i in self.token:
            token_solved += ord(i)
        result = []
        for i in text:
            result.append(ord(i) * token_solved)

        return result

    def decrypt(self, text:list):
        token_solved = 0
        for i in self.token:
            token_solved += ord(i)
        result = ""
        for i in text:
            result += chr(int(i / token_solved))

        return result
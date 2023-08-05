# picrypt
'picrypt' is a simple cryptographer.

## Install
`pip install picrypt`

## Example
```py
import picrypt

token = "banana" # you can use picrypt.generate_token() to generate a random token
encryptor = picrypt.Encryptor(token)
encrypted = encryptor.encrypt("hello world")
decrypted = encryptor.decrypt(encrypted)
print("Encrypted:", encrypted)
print("Encrypted:", decrypted)
```
Result:

```
Encrypted:  [63336, 61509, 65772, 65772, 67599, 19488, 72471, 67599, 69426, 65772, 60900]
Decrypted:  hello world
```

Use the token to encrypt and decrypt.
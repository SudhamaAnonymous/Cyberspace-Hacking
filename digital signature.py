1
2
3
4
5
6
7
8
9
10
11
12
13
import ecdsa
import hashlib
priv_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
public_key = priv_key.get_verifying_key()
message = b"HelloWorld!"
message_hash = hashlib.sha256(message).digest()
signature = priv_key.sign(message_hash)
print("The signature is:\n",signature)
try:
    public_key.verify(signature, message_hash)
    print("Signature verified: True")
except ecdsa.BadSignatureError:
    print("Signature verified: False")

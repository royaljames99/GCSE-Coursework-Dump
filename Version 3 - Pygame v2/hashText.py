import hashlib
"""
text = "YAY"
sha512 = hashlib.sha512()
sha512.update(b"YAY")
print(sha512.digest())
"""
"""
text = "ADMIN"
Sha512 = hashlib.sha512()
text = bytes(text, "ascii")
Sha512.update(text)
woo = Sha512.digest()
woo.replace(b"\\", b".")
print(woo)
"""
newPswd = "Admin"
newPswdEnc = hashlib.sha512()
newPswd = bytes(newPswd, "ascii")
newPswdEnc.update(newPswd)
newPswdEnc = str(newPswdEnc.digest()).replace("\\", ".")
print(newPswdEnc)

import secrets
import string

# secure random string
secure_str = ''.join((secrets.choice(string.ascii_letters) for i in range(10)))
print(secure_str)
# Output QQkABLyK

# secure password
password = ''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(10)))
print(password)
# output 4x]>@;4)
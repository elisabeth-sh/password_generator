import secrets
import string

def password_generator(length):
    password = ''
    material = string.ascii_letters + string.digits
    for i in range(length):
        password += "".join(secrets.choice(material))
    return password
print(password_generator(12))
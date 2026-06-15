import secrets
import string

def generate_password(length=16):

    chars = (
        string.ascii_uppercase
        + string.ascii_lowercase
        + string.digits
        + "!@#$%^&*"
    )

    return "".join(
        secrets.choice(chars)
        for _ in range(length)
    )
import hashlib
import requests

def is_breached(password):

    sha1_password = hashlib.sha1(
        password.encode()
    ).hexdigest().upper()

    prefix = sha1_password[:5]
    suffix = sha1_password[5:]

    response = requests.get(
        f"https://api.pwnedpasswords.com/range/{prefix}"
    )

    for line in response.text.splitlines():

        hash_suffix, count = line.split(":")

        if hash_suffix == suffix:
            return True

    return False
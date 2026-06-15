import re
import re

def has_repeating_chars(password):

    count = 1

    for i in range(1, len(password)):

        if password[i] == password[i - 1]:

            count += 1

            if count >= 3:
                return True

        else:
            count = 1

    return False
def has_sequential_chars(password):

    password = password.lower()

    for i in range(len(password) - 2):

        first = ord(password[i])
        second = ord(password[i + 1])
        third = ord(password[i + 2])

        if (
            second == first + 1
            and third == second + 1
        ):
            return True

    return False
def check_strength(password):

    # NEW CHECK 1
    if has_repeating_chars(password):
        return "Weak"

    # NEW CHECK 2
    if has_sequential_chars(password):
        return "Weak"

    score = 0

    if len(password) >= 12:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"\d", password):
        score += 1

    if re.search(r"[!@#$%^&*]", password):
        score += 1

    if score == 5:
        return "Strong"

    if score >= 3:
        return "Medium"

    return "Weak"
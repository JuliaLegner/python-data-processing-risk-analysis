#COMP1888 (2025-2026) Programming for Data Science
#CW1 Portfolio, Deadline 12/11/2025
#Student ID 001260070
# Portfolio Question 1a

import re
import string


def password_str(password):
    score = 0

    lgth = min(len(password), 20)
    score += lgth
    print(f"Length +{score} p. | current {score} p.")

    if re.search(r"[a-z]", password):
        score += 20
        print(f"Lowercase letters +20 p | current {score} p.")
    else:
        print("No lowercase letters, 0 p. | {score} p.")

    if re.search(r"[A-Z]", password):
        score += 20
        print(f"Uppercase letters +20p. | current {score} p.")
    else:
        print("No uppercase letters, 0 p. | current {score} p.")

    if re.search(r"[0-9]", password):
        score += 20
        print(f"Digits found +20 p | current {score} p.")
    else:
        print("No digits, 0 p.| current {score} p.")

    if any(ch in string.punctuation for ch in password):
        score += 20
        print(f"Special characters + 20 p. | current {score} p.")
    else:
        print("No special characters, 0 p.| current {score} p.")

    common_patterns = (
        "123", "234", "345", "456", "567", "678", "789",
        "abc", "bcd", "cde", "def", "efg", "fgh",
        "password", "pass", "admin", "user", "login",
        "qwerty", "asdf", "zxcv", "1234", "0000", "1111"
    )

    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 30
        print(f"Common pattern -30p | current {score} p.")
    else:
        print("No common pattern, 0 p.")

    print("-" * 40)

    final_score = max(0, min(score, 100))
    print(f"Strength score total: {final_score}/100 points\n")

    return final_score


if __name__ == "__main__":
    print("\n")
    final_password = input("Please enter your password: ").strip()
    print("-" * 40)
    strength = password_str(final_password)



    if strength <= 35:
        print(f"Your password is too weak, please try another.")
    elif strength >= 35 and strength <= 70:
        print(f"Your password is strong enough but not perfect.")
    else:
        print(f"Your password is strong enough.")

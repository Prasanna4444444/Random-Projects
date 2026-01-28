import re
import random
import string

def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add a digit")

    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        suggestions.append("Add a special character (@$!%*?&)")

    return score, suggestions


def generate_strong_password():
    characters = string.ascii_letters + string.digits + "@$!%*?&"
    password = "".join(random.choice(characters) for _ in range(12))
    return password


# ---------------- MAIN PROGRAM ----------------

print("🔐 PASSWORD STRENGTH CHECKER 🔐")
password = input("Enter your password: ")

score, suggestions = check_password_strength(password)

print("\nPassword Strength:")

if score == 5:
    print("✅ Strong Password!")
elif score >= 3:
    print("⚠️ Medium Strength Password")
else:
    print("❌ Weak Password")

if suggestions:
    print("\nSuggestions to improve:")
    for s in suggestions:
        print("-", s)

choice = input("\nDo you want a strong password generated? (yes/no): ").lower()
if choice == "yes":
    print("🔑 Generated Password:", generate_strong_password())


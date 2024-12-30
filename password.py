import re
import string
import math
import random
COMMON_WORDS = set([
    "password", "123456", "ghwerty", "admin", "letmein", "welcome", "monkey", "football", "sunshine", "iloveyou"
])

def assess_password_strength(password):
    feedback = []
    score = 0

    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    else:
        score += 1

    if not re.search(r'[a-z]', password):
        feedback.append("Password should contain at least one lowercase letter.")
    else:
        score += 1
    
    if not re.search(r'[A-Z]', password):
        feedback.append("Password should contain at least one uppercase letter.")
    else:
        score += 1
    
    if not re.search(r'[0-9]', password):
        feedback.append("Password should contain at least one digit.")
    else:
        score += 1
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("Password should contain at least one special character.")
    else:
        score += 1
    if any(common_word in password.lower() for common_word in COMMON_WORDS):
        feedback.append("Password contains common words or phrases. Consider a more unique password.")
    else:
        score += 1
    
    entropy = calculate_entropy(password)
    if entropy < 3:
        feedback.append("Password has low entropy. Consider adding more complexity.")
    else:
        score += 1
    
    if score <= 2:
        feedback.append("Password is very weak.")
    elif score == 3:
        feedback.append("Password is weak.")
    elif score == 4:
        feedback.append("Password is medium strength.")
    else:
        feedback.append("Password is strong.")

    return feedback

def calculate_entropy(password):
    unique_chars = set(password)
    n = len(password)
    entropy = 0
    for char in unique_chars:
        p = password.count(char) / n
        entropy -= p * math.log2(p)
    return entropy

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    feedback = assess_password_strength(user_password)
    
    print("\nPassword Strength Assessment:")
    for line in feedback:
        print(line)
    
    print("\nGenerated Strong Password:", generate_strong_password())

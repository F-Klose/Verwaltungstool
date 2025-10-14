import random
import string
def generate_random_password(length=8):
    Uppercase_char = random.choice(string.ascii_uppercase)
    chars = string.digits
    a = ''.join(random.choice(chars) for _ in range(length))
    special_chars = "!@#$%^&*()"
    special_chars = ''.join(random.choice(special_chars) for _ in range(1))
    final_password = Uppercase_char + a + special_chars
    print(final_password)
    return final_password

generate_random_password(8)

#TODO: print entfernen
#TODO: Gui schreiben 
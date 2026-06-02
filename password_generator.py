import random
import string
length = int(input("Enter password length: "))
if length < 1:
    print("Length must be at least 1")
else:
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    print(f"Generated Password: {password}")

print("Password requirements: minimum 8 characters, at least one number, and one uppercase letter")

attempts = 0

while attempts < 3:
    password = input("Enter password: ")

    if len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isupper() for c in password):
        print("Password accepted")
        break
    else:
        print("Password not met the requirements")
    
    attempts += 1

if attempts == 3:
    print("Maximum attempts reached")

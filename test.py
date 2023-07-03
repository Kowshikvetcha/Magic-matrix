def strength(password):
    uppercase = False
    digit = False
    for i in password:
        if i.isupper():
            uppercase = True
    for i in password:
        if i.isdigit():
            digit = True
    if len(password) >= 8 and uppercase and digit:
        print("1")
        return "Strong Password"
    else:
        print('0')
        return "Weak Password"


user_password = input("Enter a new Password: ")
print(strength(user_password))
user_password.capitalize()
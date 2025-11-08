

password = input("Enter your password: ")

if password.isdigit():
    print("Enter at least one character.")
elif password.isalpha():
    print("Enter at least one number.")
elif password.lower() == password:
    print("Enter at least one uppercase letter.")
elif password.upper() == password:
    print("Enter at least one lowercase letter.")
else:
    print("Perfect!")





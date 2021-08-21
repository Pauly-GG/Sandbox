MIN_LENGTH = 2

def password_checker ():
    password = input("Enter password of at least {} characters: ".format(MIN_LENGTH))
    while len(password) < MIN_LENGTH:
        password = input("Enter password of at least {} characters: ".format(MIN_LENGTH))

    print('*' * len(password))


password_checker()
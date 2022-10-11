from cryptography.fernet import Fernet  # import cryptography

'''
def write_key(): #write a key
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()'''

def load_key(): # load a key
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def new():  # add a new password
    domain = input("Domain: ")
    username = input("Account Name/Email: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(domain + "|" + fer.encrypt(username.encode()).decode() + "|"
                + fer.encrypt(pwd.encode()).decode() + "\n")    # writes passwords to file

def view():  # view passwords
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            domain, user, passw = data.split("|")
            print("Domain:", domain, "| User:",  # decrypts and displays passwords from file
                  fer.decrypt(user.encode()).decode(), "| Password:", fer.decrypt(passw.encode()).decode())


while True:
    mode = input("Would you like to add a new password or view existing ones (new,view), press q to quit: ").lower()
    if mode == "q":
        quit()
    elif mode == "view":
        view()
    elif mode == "new":
        new()
    else:
        print("Invalid mode.")
        continue


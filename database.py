# بسم الله
# Encrypt passwords and store them in a database, the retrieve
import sqlite3
import passwords_generator

# Create Database And Connect
db = sqlite3.connect("database.db")

db.execute(
    "create table if not exists Passwords_Manager (user_name text, password text, user_id integer)"
)
# Setting Up The Cursor
cr = db.cursor()


# the user name id
def user_name():
    user_name = input("Enter your username? : ").strip()
    return user_name


def user_id():
    user_id = int(input("What's Your ID ? : "))
    return user_id


# Done
def save_and_close():
    db.commit()
    db.close()
    print()
    print("The Connection With Database Has Just Closed")


key = 8
# print(chr(97))
# print(ord("a"))


# Encrypt and decrypt passwords
def encrypt_password(password):
    encrypted_password = ""
    for i in password:
        encrypted_password += chr(ord(i) + key)
    return encrypted_password


def decrypt_password(encrypted_password):
    decrypted_password = ""
    for i in encrypted_password:
        decrypted_password += chr(ord(i) - key)
    return decrypted_password


# en = encrypt_password("mohamed")
# print(en)
# print(decrypt_password(en))


def add_a_password_to_db(username, password, userID):
    encrypted_password = encrypt_password(password)
    cr.execute(
        f"insert into Passwords_Manager (user_name, password, user_id) values('{username}', '{encrypted_password}', '{userID}')"
    )
    print("\n*** Password stored successfully! ***\n")


def store_passwords_in_Database(pw):
    print()
    username = user_name()
    userID = user_id()
    answer = int(
        input(
            "\nDo you want to add: (1) another password? or (2) the one you have generated? "
        )
    )
    if answer == 1:
        another_password = input("\nEnter your new password: ").strip()
        add_a_password_to_db(username, another_password, userID)
    else:
        add_a_password_to_db(username, pw, userID)


def retrieve_passwords_from_Database():
    print()
    username = user_name()
    userID = user_id()
    print()
    cr.execute("select password from Passwords_Manager where user_id = ? and user_name = ?", (username, userID)
    )
    result = cr.fetchall()
    existed_passwords = []
    i = 0
    for line in result:
        for pw in line:
            dec_pw = decrypt_password(pw)
            existed_passwords.append(dec_pw)

    if len(existed_passwords) == 1:
        print(f"\nYou have already just one Password.")
        for p in existed_passwords:
            i += 1
            print(f"Your password is ==> {p}")

    elif len(existed_passwords) >= 1:
        print(f"\nYou have already {len(existed_passwords)} Passwords : ")
        for p in existed_passwords:
            i += 1
            print(f"{i} ==> {p}")
    else:
        question = (
            input(
                f"\nThis user has no passwords in our Database. Do you wanna add one? (Y/n)"
            )
            .strip()
            .lower()
        )
        if question == "y":
            q1 = int(
                input(
                    "\nDo you want us to generate you a unique password? -> press [1], or You want to add one you already have -> press [2]: "
                )
            )
            while True:
                if q1 == 1:
                    the_password = passwords_generator.return_strong_password()
                    add_a_password_to_db(username, the_password, userID)
                    break
                elif q1 == 2:
                    ps = input("\nEnter the password you want it to be stored: ")
                    add_a_password_to_db(username, ps, userID)
                    break
                else:
                    q1 = int(input("Invalid Input! Try again. [1] or [2]: "))

# Fix it later
def delete_a_password_from_db():
    print()
    username = user_name()
    userID = user_id()
    print()
    del_ps = input("Enter the password you want delete: ")
    cr.execute(
        f"select * from Passwords_Manager where user_id = '{userID}' and user_name = '{username}'"
    )
    result = cr.fetchall()
    existed_passwords = []
    i = 0
    for line in result:
        for pw in line:
            dec_pw = decrypt_password(pw)
            existed_passwords.append(dec_pw)

    if del_ps not in existed_passwords:
        print(f"Your Password : [ {del_ps} ] is not exists in your Stored Passwords.")
    else:
        cr.execute(
            f"delete from Passwords_Manager where user_id = '{userID}' and user_name = '{username}' and password = '{del_ps}'"
        )
        print()
        print(f"Your Password : [ {del_ps} ], has been deleted successfully.")


def check_for_existing_user():
    pass


def change_and_update_passwords():
    pass


# def delete_skills():
# check_skills()
# skill_name = input("Enter Your skill Name To Delete : ").strip().capitalize()
# if skill_name not in existed_skills:
#     print(f"Your skill : [ {skill_name} ] is not exists in your skills")
# else:
#     cr.execute(
#         f"delete from skills where name = '{skill_name}' and user_id = '{user_id}'"
#     )
#     print()
#     print(f"Your skill : [ {skill_name} ], has been deleted successfully.")
#     check_skills()
# save_and_close()

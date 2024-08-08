# ////////////////// بسم الله /////////////////////
import passwords_generator
import database


# def generate_a_new_password():
#     the_password = passwords_generator.return_strong_password()
#     return the_password


def store_a_password(pw):
    database.store_passwords_in_Database(pw)


new_password = "UNKNOWN"


# Main function
def main():
    while True:
        print("\n =============== Password Manager ===============")
        print("1. Generate a new password")
        print("2. Store a password")
        print("3. Retrieve your passwords")
        print("4. Update a password")
        print("5. Delete a password")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            global new_password
            new_password = passwords_generator.return_strong_password()
            print(new_password)

        elif choice == "2":
            store_a_password(new_password)

        elif choice == "3":
            database.retrieve_passwords_from_Database()
            
        elif choice == "4":
            pass
            
        elif choice == "5":
            database.delete_a_password_from_db()

        elif choice == "6":
            database.save_and_close()
            break

        else:
            print("Invalid choice. Please try again.")


# Run the password manager
if __name__ == "__main__":
    main()

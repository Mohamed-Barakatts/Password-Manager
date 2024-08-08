# ////////// بسم الله ////////////
# ===== Advanced Strong Passwords Generator =====

# if __name__ == "__main__":
import string
import random

# Setting up the password gen lists.
lower_and_upper_letters = list(string.ascii_letters)
upper_letters = list(string.ascii_uppercase)
lower_letters = list(string.ascii_lowercase)
nums_0_to_9 = list(string.digits)
punctuations = list(string.punctuation)
nums_0_to_9_and_lower_letters = nums_0_to_9 + lower_letters
nums_0_to_9_and_upper_letters = nums_0_to_9 + upper_letters
nums_0_to_9_and_lower_and_upper_letters = nums_0_to_9_and_lower_letters + upper_letters
mix_of_all = nums_0_to_9_and_lower_and_upper_letters + punctuations + list(" ")


# Check for chars num.
def chars_num():
    characters_num = input("\nHow many characters do you want for your password ?: ")
    if characters_num.isdigit() != True:  # false
        while True:
            print("Invalid Input! You can enter only Integer Numbers. Try again ...")
            characters_num = input("How many chars of your password ?: ")
            if characters_num.isdigit():
                characters_num = int(characters_num)
                break
    else:
        characters_num = int(characters_num)
    return characters_num


# Check for password options.
def password_ops():
    password_options = """\nCHOOSE THE OPTION YOU WANT FOR YOUR STRONG PASSWORD. Make it:
    1] Only Lower letters.
    2] Only Upper letters.
    3] Only Numbers.
    4] Only Punctuations.
    5] Numbers and Lower letters.
    6] Numbers and Upper letters.
    7] Lower and Upper letters.
    8] Numbers, Lower, and Upper letters.
    9] Numbers, Punctuations, Lower, and Upper letters.

    Which option do you want to make your password like?: """
    options_num = input(password_options)
    while True:
        try:
            options_num = int(options_num)
            if (options_num < 1) or (options_num > 9):
                print(
                    "Invalid Input! You can enter only Integer Numbers From [1:9], Try again ..."
                )
                options_num = int(
                    input("Which option do you want to make your password like?: ")
                )
                print()
            else:
                break
        except ValueError:
            print("\nYour option must be an Integer Number.")
            options_num = input("Enter an Integer : ")
            continue  # to check if the input can be a num or not
            print()
        except:
            print("You can only enter numbers")
            options_num = input("Enter a number of chars: ")
            continue  # to check if the input can be a num or not
            print()
    return options_num


# Shuffling the all password gen lists.
random.shuffle(lower_and_upper_letters)
random.shuffle(upper_letters)
random.shuffle(lower_letters)
random.shuffle(nums_0_to_9)
random.shuffle(punctuations)
random.shuffle(nums_0_to_9_and_lower_letters)
random.shuffle(nums_0_to_9_and_upper_letters)
random.shuffle(nums_0_to_9_and_lower_and_upper_letters)
random.shuffle(mix_of_all)

password_chars = []


# A func to return the password style as string
def get_password(num):
    random.shuffle(password_chars)
    password = ""
    print("\nYour Recommended Password is ==> ", end="")
    for i in range(num):
        password += str(password_chars[i])
    return password

# Switch case in python does not need to use "break" after each case. Like not other programming langs.
def return_strong_password():
    characters_num = chars_num()
    match password_ops():
        case 1:
            for i in range(characters_num):
                password_chars.append(lower_letters[i])
            return get_password(characters_num)

        case 2:
            for i in range(characters_num):
                password_chars.append(upper_letters[i])
            return get_password(characters_num)

        case 3:
            if characters_num > 10:
                global nums_0_to_9  # <== SI line. Declare nums_0_to_9 as a global variable
                nums_0_to_9 += nums_0_to_9

            for i in range(characters_num):
                password_chars.append(nums_0_to_9[i])
            return get_password(characters_num)

        case 4:
            for i in range(characters_num):
                password_chars.append(punctuations[i])
            return get_password(characters_num)

        case 5:
            for i in range(characters_num):
                password_chars.append(nums_0_to_9_and_lower_letters[i])
            return get_password(characters_num)

        case 6:
            for i in range(characters_num):
                password_chars.append(nums_0_to_9_and_upper_letters[i])
            return get_password(characters_num)

        case 7:
            for i in range(characters_num):
                password_chars.append(lower_and_upper_letters[i])
            return get_password(characters_num)

        case 8:
            for i in range(characters_num):
                password_chars.append(nums_0_to_9_and_lower_and_upper_letters[i])
            return get_password(characters_num)

        case _:  # default case
            for i in range(characters_num):
                password_chars.append(mix_of_all[i])
            return get_password(characters_num)


print("#" * 20, " Strong Passwords Generator ", "#" * 20, "\n")
print("\n", "#" * 22, " Thanks For Using ", "#" * 22, "\n")

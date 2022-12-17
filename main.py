# This is a sample Python script that takes  a users details and automatically generates a password.
# different functions can be created or modified
import random
import string


special_characters = list(string.ascii_letters + string.digits + "!@#$%^&*()/|;'`~-_")


# What if we did this with a customisable length
def password_gen():
    # length of password entered by user
    length = int(input("Enter password length: "))

    # A normal password should contain at-least 8 characters
    # Let's try to specify it
    if length <= 7:
        return print("Enter atleast 8 characters")

    elif length >= 8:
        print("good job!!")

        # shuffling the special_characters
        random.shuffle(special_characters)

        # picking random special_characters from the list
        password = []
        for i in range(length):
            password.append(random.choice(special_characters))

        # shuffling the resultant password
        random.shuffle(password)

        # converting the list to string
        # printing the list
        print("".join(password))
        return password_gen()
    else:
        return print("Oga is everything alright with you?😂")


password_gen()
# Press the green button in the gutter to run the script.

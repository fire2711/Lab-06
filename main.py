# adds 3 to each part of string
def encoder(password):

    encoded = ""
    # iterates over the string
    for i in range(len(password)):

        add = int(password[i]) + 3

        if add >= 10:

            add -= 10
        encoded += str(add)

    return encoded

def main():

    while True:

        # error checking
        while True:

            print("Menu \n------------- \n1. Encode  \n2. Decode  \n3. Quit ")
            print()
            choice = int(input("Select a Menu Option: "))

            if 1 <= choice <= 3:
                break

            else:
                print("Error! Invalid input.")

        # encodes with choice 1
        if choice == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored! ")

        # decodes with choice 2
        if choice == 2:
            print(f"The encoded password is {encoder(password)}, and the original password is {decoder(encoder(password))}.")

        # ends the program
        if choice == 3:
            break

if __name__ == "__main__":
    main()

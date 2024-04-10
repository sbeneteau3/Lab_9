def encoder(numbers):
    encoded_password = ''
    for digit in numbers:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        choice = int(input("Please enter an option: "))

        if choice == '1':
            password = input("Please enter your password: ")
            password_encoded = encoder('password')
            print("Your password has been encoded and stored!")
        elif choice == '2':
            pass
        elif choice == '3':
            break




if __name__ == '__main__':
    main()
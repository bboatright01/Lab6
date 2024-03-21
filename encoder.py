#Byron Boatright

# Define the function to encode the password
def encode(password):
    if not isinstance(password, str) or len(password) != 8 or not password.isdigit():
        raise ValueError("Input is not an 8-digit password containing only integers.")
    encoded = ''.join(str((int(char) + 3) % 10) for char in password)
    return encoded

def decode(encoded_password):
    if not isinstance(encoded_password, str) or len(encoded_password) != 8 or not encoded_password.isdigit():
        raise ValueError("Input is not an 8-digit password containing only integers.")
    return "".join(map(lambda c: str((int(c) - 3) % 10), encoded_password))

# Program with menu for encoding or decoding
def password_encoder_decoder_program():
    encoded = None

    while True:
        print("\nPassword Encoder/Decoder Menu:")
        print("1. Encode a password")
        print("2. Decode a password")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        # Encodes a password that the user inputs, then stores it to be decoded later
        if choice == '1':
            # Repeatedly prompts the user until they provide a valid password
            password = input("Enter an 8-digit password to encode: ")
            while len(password) != 8 or not password.isdigit():
                print("Please input a valid password")
                password = input("Enter an 8-digit password to encode: ")

            encoded = encode(password)
            print(f"Encoded Password: {encoded}")
            print("Stored encoded password!")

        # Decodes the password that the user provided earlier
        elif choice == '2':
            if encoded == None:
                print("Encode a password first!")
                continue
            decoded = decode(encoded)
            print(f"The encoded password is: {encoded}, and the original password is: {decoded}.")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Defines the main function
def main():
    password_encoder_decoder_program()

# Check if the script is run directly (not imported) and then call main
if __name__ == "__main__":
    main()

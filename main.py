def encode(password):
    encoded_list = []
    for char in password:
        encoded_char = str(int(char) + 3)
        if int(encoded_char) > 9:
            encoded_char = str(int(encoded_char) - 10)
        encoded_list.append(encoded_char)
    encoded_password = ''.join(encoded_list)
    return encoded_password

def decode(encoded_password):
    decoded_list = []
    for char in encoded_password:
        decoded_char = str(int(char) - 3)
        decoded_list.append(decoded_char)
    decoded_password = ''.join(decoded_list)
    return decoded_password

if __name__ == "__main__":
    program_quit = False

    while not(program_quit):

        print('Menu:\n'
          '-----\n'
          '1. Encode Password\n'
          '2. Decode Password\n'
          '3. Quit\n')

        user_input = input('Select an option: ')

        if user_input == '1':
            new_password = encode(input('Enter password: '))
            print(f'Your encoded password is: {new_password}\n')

        elif user_input == '2':
            pass
        elif user_input == '3':
            program_quit = True
            break

        else:
            print('Invalid selection. Try again.\n')
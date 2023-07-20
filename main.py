#Lucas Nardin
def encode(password):
    encoded_list = []
    for char in password:
        encoded_char = str(int(char) + 3)
        if int(encoded_char) > 9:
            encoded_char = str(int(encoded_char) - 10)
        encoded_list.append(encoded_char)
    encoded_password = ''.join(encoded_list)
    return encoded_password

if __name__ == "__main__":
    program_quit = False

    while not(program_quit):

        print('Menu:\n'
          '-------------\n'
          '1. Encode\n'
          '2. Decode\n'
          '3. Quit\n')

        user_input = input('Please enter an option: ')

        if user_input == '1':
            password = encode(input('Please enter your password to encode: '))
            print(f'Your password has been encoded and stored!\n')

        elif user_input == '2':
            pass
        elif user_input == '3':
            program_quit = True
            break

        else:
            print('Invalid selection. Try again.\n')

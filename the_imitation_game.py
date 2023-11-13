decrypted_message = input()
command = input()
while command != "Decode":
    some_move = command.split("|")

    if some_move[0] == "Move":
        number_of_letters = some_move[1]
        number_of_letters = int(number_of_letters)
        decrypted_message = f"{decrypted_message[number_of_letters:]}{decrypted_message[:number_of_letters]}"

    elif some_move[0] == "Insert":
        index, value = some_move[1], some_move[2]
        index = int(index)
        decrypted_message = f"{decrypted_message[:index]}{value}{decrypted_message[index:]}"

    elif some_move[0] == "ChangeAll":
        substring, replacement = some_move[1], some_move[2]
        decrypted_message = decrypted_message.replace(substring,replacement)

    command = input()

print(f"The decrypted message is: {decrypted_message}")



#TODO: Create a letter using starting_letter.txt

with open("./Input/Names/invited_names.txt") as file:
    name_list = file.readlines()

with open("./Input/Letters/starting_letter.txt") as file:
    contents = file.read()
    for x in name_list:
        new_letter = contents.replace("[name]", x.strip())
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{x.strip()}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

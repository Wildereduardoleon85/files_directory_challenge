names_list = []
starting_letter_content = ""

with open("./Input/Names/invited_names.txt") as invited_names:
    content = invited_names.read()
    names_list = content.split()

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    content = starting_letter.read()
    starting_letter_content = content


for name in names_list:
    content = starting_letter_content.replace("[name]", name)

    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as output_letter:
        output_letter.write(content)

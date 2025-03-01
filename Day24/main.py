# file=open("Day24/my_file.txt")
# contents=file.read()
# print(contents)
# file.close()

# with open("Day24/my_file.txt",mode="a") as file:
#     file.write("\n New text.")

# with open ("Day24/new_file.txt",mode="w") as file:
#     file.write("Hello jarvis")

# with open("/Users/shubh/OneDrive/Documents/new_file.txt") as file:
#     contents=file.read()
#     print(contents)





PLACEHOLDER="[name]"
with open("Day24/input/Names/invited_names.txt") as names_file:
    names=names_file.readlines()
    

with open("Day24/input/Letters/starting_letter.docx") as letter_file:
    letter_contents=letter_file.read()
    for name in names:
        stripped_name=name.strip()
        new_letter=letter_contents.replace(PLACEHOLDER,stripped_name)
        with open("Day24/Output/ReadyToSend/letter_for_{stripped_name}.docx",mode="w") as completed_letter:
            completed_letter.write(new_letter)
# IMPORTS
from file_manager import FileManager
#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# Initialize the file_manager
file_manager = FileManager()

# Retrieve invite list and set it equal to a variable as a list
invited_names_content = file_manager.read_file(relative_path="Input/Names/invited_names.txt")
invite_list = invited_names_content.split("\n")
# print(invite_list)

# Retrieve template letter and set it equal to a variable
letter_template_content = file_manager.read_file(relative_path="Input/Letters/letter_template.txt")
# print(starting_letter_content)

for each_name in invite_list:
    # Replace each "[name]" string with the list of names and write each new_letter to a directory
    new_letter_content = letter_template_content.replace("[name]", each_name)
    # print(new_letter_content)
    new_filename = each_name + "_invite.txt"
    # print(new_letter_filename)
    file_manager.write_to_file(relative_path="Output/ReadyToSend", new_file_name=new_filename, content=new_letter_content)
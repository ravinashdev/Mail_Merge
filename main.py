# IMPORTS
from file_manager import FileManager
#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# Initialize the file_manager
file_manager = FileManager()

# Retrieve invite list and set it equal to a variable
invited_names_content = file_manager.read_file("Input/Names/invited_names.txt")
invite_list = invited_names_content.split("\n")
# print(invite_list)

# Retrieve template letter and set it equal to a variable
starting_letter_content = file_manager.read_file("Input/Letters/starting_letter.txt")
# print(starting_letter_content)

for each_name in invite_list:
    # Replace each "[name]" string with the list of names and write each new_letter to a directory
    new_letter_content = starting_letter_content.replace("[name]", each_name)
    # print(new_letter_content)
    new_letter_filename = each_name + "_invite.txt"
    # print(new_letter_filename)
    # file_manager.write_to_file("Output/ReadyToSend", new_letter_content, )
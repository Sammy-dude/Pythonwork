# # Open the file in write mode
# with open('test123.txt', 'w') as file:
#     # Write the sentence to the file
#     file.write("Thank you for considering my application. I would welcome the opportunity to discuss how my background and experience can contribute.")
#
#     content= file.read()
#     if "considering my application" in content:
#         print("value found"+ content);
#     else:
#         print("value not found " + content);
# with open('test123.txt', 'a') as file:
#     file.write(" You can retrieve the file path, name")
# # The file is automatically closed after the 'with' block
from datetime import datetime


# Open the file in write mode to write the initial content
def get_timestamp():
    # Get the current date and time, and format it as needed
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# f"\n[{get_timestamp()}]

with open('test123.txt', 'a') as file:
    # Write the sentence to the file
    file.write(f"\n[{get_timestamp()}]\nThank you for considering my application. I would welcome the opportunity to discuss how my background and experience can contribute")

# Open the file in read mode to check for the string
with open('test123.txt', 'r') as file:
    content = file.read()  # Read the content of the file

    # Check if "considering my application" exists in the content
    if "considering my application" in content:
        print("Value found: " + content)
    else:
        print("Value not found: " + content)

# Open the file in append mode to add the new sentence
with open('test123.txt', 'a') as file:
    file.write(" \nYou can retrieve the file path, name\n")

# Re-open the file in read mode to print the final content
with open('test123.txt', 'r') as file:
    final_content = file.read()  # Read the updated content

print("Updated file content:")
print(final_content)

import os

# Specify the file name
file_name = 'test123.txt'
# file_name.find('test123.txt',set)
# Get the absolute path of the file
file_path = os.path.abspath(file_name)

# Get the file size (in bytes)
file_size = os.path.getsize(file_name)

# Check if the file exists
file_exists = os.path.exists(file_name)

# Print file information
print(f"File Name: {os.path.basename(file_name)}")
print(f"File Path: {file_path}")
print(f"File Size: {file_size} bytes")
print(f"File Exists: {file_exists}")

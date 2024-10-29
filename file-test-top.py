from datetime import datetime


# Function to get the current timestamp
def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Open the file in read mode to get the current content
with open('test123.txt', 'r') as file:
    original_content = file.read()

# Open the file in write mode to overwrite it with new content at the top
with open('test123.txt', 'w') as file:
    # Write the new content (appending to the top)
    file.write(
        "[" + get_timestamp() + "] " + "Thank you for considering my application. I would welcome the opportunity to discuss how my background and experience can contribute.\n")

    # Write the original content back to the file
    file.write(original_content)

# Re-open the file in read mode to print the final content
with open('test123.txt', 'r') as file:
    final_content = file.read()  # Read the updated content

print("Updated file content:")
print(final_content)

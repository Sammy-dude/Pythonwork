
import os
import platform

# Get the current working directory
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

# List all files and directories in the current directory
files = os.listdir(current_directory)
print(f"Files and Directories: {files}")
print("\n"+os.name+"\n ")
system_info = platform.system()
release_info = platform.release()
version_info = platform.version()

print(f"Platform: {system_info}")
print(f"Release: {release_info}")
print(f"Version: {version_info}")

env_vars = os.environ
print(f"Environment Variables: {env_vars}")
for key, value in os.environ.items():
    print(f'{key}: {value}')
# Create a new directory
# os.mkdir('new_folder')
print(os.environ.get("USER"))
print(os.getenv("USER"))
# Get an environment variable (e.g., PATH)
path_var = os.getenv('PATH')
print(f"PATH: {path_var}")
os.getenv("USER")
# Change directory
# os.chdir('new_folder')

my_list = [1, 2, 3]
my_list1= my_list.copy()
my_list1.append([4,5,6])
# Use dir() to see what the list object can do
print(my_list1)
print(dir(my_list))
print(help(my_list))
print(help(my_list.append))





#print(f"Changed Directory: {os.getcwd()}")

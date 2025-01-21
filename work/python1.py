import os

directory_name = "python_practice_git"

# Create the directory if it doesn't exist
if not os.path.exists(directory_name):
    os.makedirs(directory_name)

# Check if the directory was created
print(os.path.exists(directory_name))

import os

# # Create a new directory
# os.mkdir("my_new_directory")

# Change the current working directory
os.chdir("my_new_directory")

# # Get the current working directory
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

# List the contents of the current directory (initially empty)
print(f"Contents of {current_dir}: {os.listdir(current_dir)}")

# Create a file
with open("my_file.txt", "w") as f:
    f.write("Hello from os module!")

# List the contents again
print(f"Contents after creating file: {os.listdir(current_dir)}")

# Check if the file exists
if os.path.exists("my_file.txt"):
    print("my_file.txt exists.")

# Access an environment variable (e.g., HOME on Unix-like systems)
home_dir = os.environ.get("HOME")
if home_dir:
    print(f"Home directory: {home_dir}")

# Go back to the parent directory
os.chdir("..")

# Remove the file
os.remove("my_new_directory/my_file.txt")

# Remove the directory
os.rmdir("my_new_directory")
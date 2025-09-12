# The Python pathlib module provides an object-oriented approach to handling filesystem 
# paths, offering a more intuitive and "Pythonic" way to interact with the file system 
# compared to the traditional os module.

from pathlib import Path

# Get the current working directory
current_dir = Path.cwd()
print(f"Current directory: {current_dir}")

# Create a new path
new_file_path = current_dir / "my_folder" / "my_file.txt"
print(f"New file path: {new_file_path}")

# Check if a path exists
if new_file_path.exists():
    print("File exists.")
else:
    print("File does not exist.")

# Create directories
new_file_path.parent.mkdir(parents=True, exist_ok=True)

# Write to a file
new_file_path.write_text("Hello, pathlib!")

# Read from a file
content = new_file_path.read_text()
print(f"File content: {content}")

# Delete the file
new_file_path.unlink()
print(f"File deleted: {new_file_path}")
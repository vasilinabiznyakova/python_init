from pathlib import Path
import shutil

# Create a Path object for a directory
# directory = Path("./4")

# # List all files and subdirectories
# for path in directory.iterdir():
#     print(path)


# Path.mkdir(mode=0o777, parents=False, exist_ok=False) # mode is for Linux only

directory = Path("new_folder")
directory.mkdir(parents=True, exist_ok=True)


# Check for existence
if directory.exists():
    print(f"{directory} exists")

# Check for directory
if directory.is_dir():
    print(f"{directory} is a directory")

# Check for file
if directory.is_file():
    print(f"{directory} is a file")


# Current work dir
dir = Path.cwd()

# Absolute path
dir_a = dir.absolute()

print(dir)
print(dir_a)

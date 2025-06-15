from pathlib import Path

# Create a Path object for a directory
directory = Path("./4")

# List all files and subdirectories
for path in directory.iterdir():
    print(path)


Path.mkdir(mode=0o777, parents=False, exist_ok=False) # mode is for Linux only

directory = Path("/new_folder")
directory.mkdir(parents=True, exist_ok=True)

import shutil

"""
The shutil module in Python is a standard library module that provides a number of functions for working with files and collections of files. This module can be used to copy, move, rename, and delete files and directories, providing high-level operations for handling the file system that are more convenient than using the basic functions of the os module.
The shutil package supports zip, tar, and gz archives. It uses the zipfile and tarfile packages to do this

shutil.make_archive(base_name, format, root_dir=None, base_dir=None)

"""


# # Create a ZIP archive with the contents of the 'my_folder' directory
# shutil.make_archive("example", "zip", root_dir="4")


# # Unpacking a ZIP archive to a specific directory
# shutil.unpack_archive("example.zip", "destination_folder")


# # Copy the file
# source_file = "/path/to/source/file.txt"
# destination_dir = "/path/to/destination"
# shutil.copy(source_file, destination_dir)

# # Copy the entire directory
# source_dir = "/path/to/source/directory"
# destination_dir = "/path/to/destination/directory"
# shutil.copytree(source_dir, destination_dir)

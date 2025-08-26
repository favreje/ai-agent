import os

from .config import MAX_CHARS


def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    abs_file_path = os.path.abspath(full_path)

    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}\n"'

    abs_working_directory = os.path.abspath(working_directory) + os.sep
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory\n'

    try:
        with open(abs_file_path, "r") as f:
            file_contents = f.read(MAX_CHARS)
    except FileNotFoundError:
        return "Error: File not found"
    except PermissionError:
        return "Error: Cannot read file"

    if len(file_contents) == MAX_CHARS:
        appendage = f'\n[... File "{file_path} truncated at 10,000 characters]'
        file_contents = file_contents + appendage
    return file_contents

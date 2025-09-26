import os

from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    abs_file_path = os.path.abspath(full_path)

    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}\n"'

    abs_working_directory = os.path.abspath(working_directory) + os.sep
    if not abs_file_path.startswith(abs_working_directory):
        return (
            f'Error: Cannot read "{file_path}" as it is outside the permitted working directory\n'
        )

    try:
        with open(abs_file_path, "r", encoding="utf-8", errors="replace") as f:
            # read an additional character so that we can later check if the file is larger
            # than MAX_CHARS and truncate to exactly MAX_CHARS in our return message
            file_contents = f.read(MAX_CHARS + 1)
    except FileNotFoundError:
        return "Error: File not found"
    except PermissionError:
        return "Error: Cannot read file"

    if len(file_contents) > MAX_CHARS:
        file_contents = file_contents[:MAX_CHARS]
        appendage = f'\n[... File "{file_path} truncated at {MAX_CHARS} characters]'
        file_contents = file_contents + appendage
    return file_contents

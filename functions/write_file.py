import os


def write_file(working_directory, file_path, content):

    full_path = os.path.join(working_directory, file_path)
    abs_file_path = os.path.abspath(full_path)
    abs_working_directory = os.path.abspath(working_directory) + os.sep
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    # reject paths that look like directories (no basename)
    if os.path.basename(abs_file_path) == "":
        return f'Error: "{file_path}" is a directory, not a file'

    # if target exists, but is a directory -> error
    if os.path.isdir(abs_file_path):
        return f'Error: "{file_path}" is a directory, not a file'

    try:
        os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
    except Exception as e:
        return f"Error: Could not create directory - {e}"

    try:
        with open(abs_file_path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        return "Error: File write error - {e}"

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

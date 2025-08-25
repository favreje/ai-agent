import os


def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    abs_directory = os.path.abspath(full_path) + os.sep

    if not os.path.isdir(abs_directory):
        return f'Error: "{directory}" is not a directory\n'

    abs_working_directory = os.path.abspath(working_directory) + os.sep
    if not abs_directory.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory\n'

    dir_contents = ""
    for object in os.listdir(abs_directory):
        full_path = os.path.join(abs_directory, object)
        name = object
        file_size = os.path.getsize(full_path)
        is_dir = os.path.isdir(full_path)
        contents = f"- {name}: file_size={file_size} bytes, is_dir={is_dir}"
        dir_contents = "".join(dir_contents + contents)
        dir_contents = dir_contents + "\n"
    return dir_contents

import subprocess
import os


def run_python_file(working_directory, file_path, args=None):
    full_path = os.path.join(working_directory, file_path)
    abs_file_path = os.path.abspath(full_path)
    abs_working_directory = os.path.abspath(working_directory) + os.sep
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    # reject paths that look like directories (no basename)
    if os.path.basename(abs_file_path) == "":
        return f'Error: "{file_path}" is a directory, not a file'

    # if target exists, but is a directory -> error
    if os.path.isdir(abs_file_path):
        return f'Error: "{file_path}" is a directory, not a file'

    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found'

    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'

    TIMEOUT = 30
    if args is None:
        args = []
    params = ["uv", "run", abs_file_path] + args

    try:
        result = subprocess.run(
            params,
            capture_output=True,
            text=True,
            timeout=TIMEOUT,
            cwd=abs_working_directory,
        )

        if not result.stderr and not result.stdout and result.returncode != 0:
            return "No output produced"

        metadata = ""
        if result.stdout:
            metadata += f"STDOUT: {result.stdout}"
        if result.stderr:
            metadata += f"\nSTDERR: {result.stderr}"
        if result.returncode != 0:
            metadata += f"\nProcess exited with code {result.returncode}"

        return metadata

    except Exception as e:
        return f"Error: Python file could not be executed - {e}"

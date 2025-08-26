from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


working_dir = "calculator"
test_file = ("main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py")
for i, file in enumerate(test_file, start=1):
    print(f"Test {i}\nResult for file: {file}")
    print(get_file_content(working_dir, file))

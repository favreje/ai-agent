from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


print("--- Start of Tests for get_files_info Function ---\n")
working_dir = "calculator"
test_dir = (".", "pkg", "/bin", "../", "does_not_exist")
for i, dir in enumerate(test_dir, start=1):
    print(f"Test {i}\nResult for {dir} directory:")
    print(get_files_info(working_dir, dir))
print("--- End of Tests for get_files_info Function ---")
print()
print("--- Start of Tests for get_file_content Function ---\n")

contents = get_file_content(working_dir, "lorem.txt")
print(contents)
print("--- End of Tests for get_file_content Function ---\n")

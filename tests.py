from functions.get_files_info import get_files_info


working_dir = "calculator"
test_data = (".", "pkg", "/bin", "../")


for dir in test_data:
    print(f"Result for {dir} directory:")
    results = get_files_info(working_dir, dir)
    print(results)

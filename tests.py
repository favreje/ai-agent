from functions.run_python_file import run_python_file


working_dir = "calculator"
cases = (
    ("main.py", None),
    ("main.py", ["3 + 5"]),
    ("tests.py", None),
    ("../main.py", None),
    ("nonexistent.py", None),
    ("lorem.txt", None),
)
for i, (file, args) in enumerate(cases, start=1):
    print(f"Test {i}\nResult for file: {file}")
    print(run_python_file(working_dir, file, args))
    print()

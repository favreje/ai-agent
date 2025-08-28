from functions.write_file import write_file


working_dir = "calculator"
cases = (
    ("lorem.txt", "wait, this isn't lorem ipsum"),
    ("pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    ("/tmp/temp.txt", "this should not be allowed"),
)
for i, (path, content) in enumerate(cases, start=1):
    print(f"Test {i}\nResult for file: {path}")
    print(write_file(working_dir, path, content))
    print()

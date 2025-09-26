from google.genai import types

from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from config import WORKING_DIR

func_register = {
    "get_file_content": get_file_content,
    "get_files_info": get_files_info,
    "write_file": write_file,
    "run_python_file": run_python_file,
}


def call_function(func_call: types.FunctionCall, verbose: bool = False) -> types.Content:
    if verbose:
        print(f"Calling function: {func_call.name}({func_call.args})")
    else:
        print(f"Calling function: {func_call.name}")

    name_str = func_call.name
    if not name_str:
        name_str = ""

    func = func_register.get(name_str)
    args = func_call.args or {}

    if not func:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=name_str,
                    response={"error": f"Unknown function: {name_str}"},
                )
            ],
        )

    try:
        result = func(WORKING_DIR, **args)
    except Exception as e:
        print(f"Error: {e}")
        return types.Content()

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=name_str,
                response={"result": result},
            )
        ],
    )

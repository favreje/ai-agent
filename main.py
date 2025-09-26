import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from generate_content import generate_content


def main():
    # Get prompt from user. If no prompt is provided, exit without calling the API
    args = sys.argv[1:]
    if not args:
        print("Gemini AI Code Assistant")
        print('\nUsage: py main.py "your prompt here"')
        print('Example: py main.py "How do I fix the calculator?"')
        sys.exit(1)
    is_verbose = "--verbose" in args
    prompt_args = [arg for arg in args if not arg.startswith("--")]
    user_prompt = " ".join(prompt_args)
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # Create an instance of the Gemini client
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    generate_content(
        client=client,
        messages=messages,
        user_prompt=user_prompt,
        is_verbose=is_verbose,
    )


if __name__ == "__main__":
    main()

import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt


def generate_content(client, messages, user_prompt, is_verbose):
    # Retrieve a response and display it, along with token count metadata
    model = "gemini-2.0-flash-001"
    response = client.models.generate_content(
        model=model,
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )

    print("-" * 100)
    print("AI Agent")
    print("-" * 100)
    print(response.text)
    print("-" * 100)

    if is_verbose:
        print(f"Model: {model}")
        print(f"User prompt: {user_prompt}")
        if response.usage_metadata:
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        else:
            print("Usage metadata not available")


def main():
    # get prompt from user. if no prompt is provided, exit without calling the API
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

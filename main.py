import os
import sys
from dotenv import load_dotenv
from google import genai


def main():
    # Get prompt from user. If not prompt provided, exit gracefully without calling the API
    args = sys.argv[1:]
    if not args:
        print("Gemini AI Code Assistant")
        print('\nUsage: py main.py "your prompt here"')
        sys.exit(1)
    prompt = " ".join(args)

    # Create an instance of the Gemini client
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # Retrieve a response and display it, along with token count metadata
    model = "gemini-2.0-flash-001"
    response = client.models.generate_content(model=model, contents=prompt)
    print("-" * 100)
    print("AI Agent")
    print("-" * 100)
    print(f"Model: {model}")
    print(f"Prompt: {prompt}")
    print()
    print(response.text)

    print()
    print("-" * 100)
    if response.usage_metadata:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        print("Usage metadata not available")


if __name__ == "__main__":
    main()

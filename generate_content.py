from google.genai import types

from functions.schemas import available_functions
from functions.call_function import call_function
from prompts import system_prompt


def generate_content(client, messages, user_prompt, is_verbose):
    # Retrieve a response and display it, along with token count metadata
    model = "gemini-2.0-flash-001"
    response = client.models.generate_content(
        model=model,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )

    print("-" * 100)
    print("AI Agent")
    print("-" * 100)

    if not response.function_calls:
        return response.text

    function_responses = []
    for function_call in response.function_calls:
        result = call_function(function_call, is_verbose)
        if not result.parts or not result.parts[0].function_response:
            raise Exception("Empty function call result")

        this_response = result.parts[0].function_response.response

        print("-" * 100)
        if is_verbose:
            print(f"Model: {model}")
            print(f"User prompt: {user_prompt}")
            if response.usage_metadata:
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            print(f"-> {this_response}")
        function_responses.append(this_response)

    if not function_responses:
        raise Exception("No function responses generated. Exiting.")

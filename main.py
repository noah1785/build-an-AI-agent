import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types


def main():
    print("Hello from build-an-ai-agent!")

    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set")


    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    # Now we can access `args.user_prompt`

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    content = args.verbose
    # content = args.user_prompt
    # content = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    # response = client.models.generate_content(model='gemini-2.5-flash', contents=content)
    response = client.models.generate_content(
    model="gemini-2.5-flash", contents=messages
)
    
    if response.usage_metadata == None:
    
        raise RuntimeError("failed API request")
    
    else:

    #     prompt_tokens = f"Prompt tokens: {response.usage_metadata.prompt_token_count}"
    #     response_tokens = f"Response tokens: {response.usage_metadata.candidates_token_count}"
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count

    #     print(prompt_tokens)
    #     print(response_tokens)
        if content:
            display_user_prompt = f"User prompt: {args.user_prompt}"
            prompt_tokens_str = f"Prompt tokens: {prompt_tokens}"
            response_tokens_str = f"Response tokens: {response_tokens}"

            print(display_user_prompt)
            print(prompt_tokens_str)
            print(response_tokens_str)
            print(response.text)

        else:
            
            print(response.text)
    # print(response.text)


if __name__ == "__main__":
    main()

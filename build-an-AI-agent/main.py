import os
from dotenv import load_dotenv
from google import genai
import argparse


def main():
    print("Hello from build-an-ai-agent!")

    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set")


    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    # Now we can access `args.user_prompt`

    content = args.user_prompt
    # content = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    response = client.models.generate_content(model='gemini-2.5-flash', contents=content)
    
    if response.usage_metadata == None:
    
        raise RuntimeError("failed API request")
    
    else:

        prompt_tokens = f"Prompt tokens: {response.usage_metadata.prompt_token_count}"
        response_tokens = f"Response tokens: {response.usage_metadata.candidates_token_count}"

        print(prompt_tokens)
        print(response_tokens)

    print(response.text)


if __name__ == "__main__":
    main()

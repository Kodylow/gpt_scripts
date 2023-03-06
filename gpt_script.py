#!/usr/bin/env python
import argparse
import datetime
import json
import os

import openai

# Set up the OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Set up command line argument parser
parser = argparse.ArgumentParser(
    description="Send a question to the GPT-3 API.")
parser.add_argument("question", nargs="+",
                    help="The question to send to the API.")

# Parse command line arguments
args = parser.parse_args()

# Combine all command line arguments into a single string
question = " ".join(args.question)

# Add a question mark to the end of the question if it's missing
if not question.endswith("?"):
    question += "?"

# Call the OpenAI API with the user's question
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a Linux, Bash, Git, Nix, and 'all things command line' expert. You give short, precise answers to questions by returning just a python or bash script that will solve the problem whenever possible. The user just wants the script and nothing else."},
        {"role": "user", "content": question}
    ]
)

# Extract the response text from the API response
answer = response["choices"][0]["message"]["content"]

# Print the answer to the console
print(answer)

with open("gpt_log.txt", "a") as f:
    now = datetime.datetime.now()
    log_entry = f"{now}: {question}\n{now}: {answer}\n"
    f.write(log_entry)

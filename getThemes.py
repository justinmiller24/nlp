# This script is used to extract themes from qualitative data
# Written by Justin Miller on 5.14.2024
#
# Make sure the Python OpenAI library is installed
# pip install openai
#
# Linux script usage
# python getSurveyThemes.py data.csv sk-XXXXXX > output.txt

# Load Libraries
from openai import OpenAI
import pandas as pd
import sys

# Make sure filename and OpenAI key exists
if len(sys.argv) < 3:
    print("Error: missing arguments")
    sys.exit(1)

# Load survey responses
# Read these from CSV file, passed in as first arg in script
# Parse these using the pandas library, and concatenate into a combined string
# The combined string will be fed into OpenAI to run text analysis
df = pd.read_csv(sys.argv[1])
df = df.astype(str)
comments = df['original'].str.cat()

# Use the OpenAI GPT-3.5 Turbo model, it is fast and inexpensive for simple tasks
# Max content length is 16k
client = OpenAI(api_key = sys.argv[2])
response = client.completions.create(
    model = "gpt-3.5-turbo",
    prompt = f"Identify the top 5 themes discussed in the following survey responses: {comments}",
    max_tokens = 150
)

# Parse and return the themes
print(response.choices[0].message.content)



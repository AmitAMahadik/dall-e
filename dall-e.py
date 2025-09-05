import os
from openai import OpenAI
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

# Example request
print(openai.models.list())

client = OpenAI()

# Create shopping list and recipe function
def create_shopping_list(recipe):
    prompt = f"Create a shopping list for the following recipe:\n\n{recipe}\n\nShopping List:"
    return prompt

# Function test
recipe = create_shopping_list("Chipotle Chicken with Rice bowl")

print(recipe)

# Reaching out to OpenAI for the answer
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": recipe}
    ],
    temperature=0.7,
    top_p=1,
)
print(response.choices[0].message.content)

# Putting the ingredients into a shopping list
import re
text = response.choices[0].message.content

pattern = re.compile(r'[-\d.]+\s*(.+)')
matches = pattern.findall(text)

shopping_list = []
for match in matches:
    shopping_list.append(match)


print(shopping_list)

# Generate an image using DALL-E 3
response = client.images.generate(
    model="dall-e-3",
    prompt=shopping_list[2],
    size="1024x1024",
    quality="standard",
    n=1
)

image_url = response.data[0].url

print(f"Generated image URL: {image_url}")


import requests
import json

OPENAI_API_KEY = ""

prompt_init = """in the context of the food recipe here is a person describing how to create this recipe,  can you provide what is he/ she preparing and also get the scenes for replicating the steps? from the below description.
give an explanation for each step, follow the heading and body structure
if there are multiple steps in a single step use arrays in the output json
{
"title": "name of the dish"
"description": "describe about the recipe"

"instructions":[ { "heading": "blah blah",
  "body":  {"highlights": "highlight of this step, keep it about than 10 words not less than 5 words",
"explanation":" Elaborate in more than 50 words" 
}]
}"
here is the description:
"""
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + OPENAI_API_KEY  # Replace with your actual API key
}

def getInstructions(transcript):
    prompt = prompt_init + "\n" + "Hi, I'm Jacques Pepin, and I'm cooking at home. This is a small easy dessert done with guava paste, inspired by my wife, you know, Spanish background, Puerto Rican. So what I'm using here, a regular pound cake here that you can buy. You know, a small slice about, not quite half an inch wide. I'm trimming it. Although you don't have to trim it. Cut it in 4. Okay. Put that here. So So here we do that for like 12. And even if you trim it, don't throw that away. Okay. Here we are. You can do that, of course. I'm doing guava paste, but you can use other type of dry fruit. So I have the guava here. Sometime it come in can. Sometime it come in block like this. And of course, this is concentrale taste. So I am, turning that into about half inch stick. Yeah. You can do them smaller than that or bigger than that. And I'm doing like 3 piece like this. 1, 2, 3. Okay. Then on top of this, I put a little bit of cream cheese. This is, you know, Those are just whipped cream cheese, yeah? I like the whipped cream cheese, but you can have any cream cheese you want this. And on top of this, of course, mint. And the mint here, I have in my garden a lot of meat, but it's not really a decoration. You have to eat that piece until the leaves of meat goes so well with that picture of cream cheese and so. And this is it, you know, presenting it this way. Can even put a few little pieces of mint around, and So this is this for my wife, Gloria, cream cheese and guava paste, and you can serve it on cookie, easy on pancake. I'm sure you're going to like it. Happy cooking.\"" 
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        # Parse the JSON response
        response_data = response.json()

        # Print the parsed data
        response_str = response_data['choices'][0]['message']['content']
        response_json = json.loads(response_str)
        return response_json
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code}, {response.text}")
        return None
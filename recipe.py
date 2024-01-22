import requests
import json

OPENAI_API_KEY = ""

prompt_init = """in the context of the food recipe here is a person describing how to create this recipe,  can you provide what is he/ she preparing and also get the scenes for replicating the steps? from the below description.
give an explanation for each step, follow the given valid output JSON structure for heading and body structure
{
    "title": "name of the dish",
    "description": "describe about the recipe",
    "instructions":[
        {
            "heading": "blah blah",
            "body": {
                "highlights": "highlight of this step, keep it about than 10 words not less than 5 words",
                "explanation": "Elaborate in more than 50 words",
            },
        },
    ],
};

here is the description:
"""
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + OPENAI_API_KEY  # Replace with your actual API key
}

async def getInstructions(transcript):
    prompt = prompt_init + "\n" + transcript 
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            response_data = response.json()

            response_str = response_data['choices'][0]['message']['content']
            response_json = json.loads(response_str)
            return response_json
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None
    except Exception as error:
        print(error)
        

import requests
import os
from dotenv import load_dotenv

#importing API-KEY from .env
load_dotenv()
API_KEY = os.getenv('API_KEY')


REQUEST_URL = "https://api.api-ninjas.com/v1/animals?name="
OUTPUT_FILE_NAME = "output.html"


def save_to_file(text, file_name):
    with open(file_name, "w") as handle:
        handle.write(text)

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
          ...
        },
        'locations': [
          ...
        ],
        'characteristics': {
         ...
    }
    },
    """
    res = requests.get(REQUEST_URL + animal_name, headers={'X-Api-Key': API_KEY})
    data = res.json()
    save_to_file(res.text, OUTPUT_FILE_NAME)
    print(res.text)

    if isinstance(data, list):
        return data
    else:
        print(f"Unexpected response format: {data}")
        return []
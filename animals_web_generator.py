import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


with open("animals_template.html", "r", encoding="utf-8") as file:
    html_content = file.read()


print(html_content)
animals_data = load_data('animals_data.json')

output = "" # define an empty string
for animal in animals_data:
    output += '<li class="cards__item">'
    output += f'Name: {animal["name"]}<br/>\n'
    output += f'Diet: {animal["characteristics"]["diet"]}<br/>\n'
    output += f'Location: {animal["locations"][0]}<br/>\n'
    try:
        output += f'Type: {animal["characteristics"]["type"]}<br/>\n'
        output += '<li/><br/>\n'
    except KeyError:
        output += f'<li/><br/>\n'

filler_txt = "__REPLACE_ANIMALS_INFO__"
website_txt = html_content.replace(filler_txt, output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(website_txt)

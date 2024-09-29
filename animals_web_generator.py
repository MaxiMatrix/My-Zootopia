import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


with open("animals_template.html", "r", encoding="utf-8") as file:
    html_content = file.read()


animals_data = load_data('animals_data.json')

output = "" # define an empty string
for animal in animals_data:
    output += f'<li class="cards__item">'
    output += f'<div class="card__title">{animal["name"]}</div>\n'
    output += f'<p class="card__text">'
    output += f'<strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'
    output += f'<strong>Location:</strong> {animal["locations"][0]}<br/>\n'
    try:
        output += f'<strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'
        output += f'</p>\n'
        output += f'</li>\n'
    except KeyError:
        output += f'</p>\n'
        output += f'</li>\n'


filler_txt = "__REPLACE_ANIMALS_INFO__"
website_txt = html_content.replace(filler_txt, output)


with open("animals.html", "w", encoding="utf-8") as file:
    file.write(website_txt)

print(output)
import data_fetcher


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:  # Ensure UTF-8 encoding for JSON file
        return json.load(handle)


def serialize_animal(animal_obj):
    """Serializes an animal object into an HTML list item"""
    output = f'<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'
    output += f'  <p class="card__text">\n'
    output += f'    <strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'
    output += f'    <strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'

    try:
        output += f'    <strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'
    except KeyError:
        pass  # Handle case where 'type' is missing

    output += f'  </p>\n'
    output += f'</li>\n'
    return output


def main():
    # Read the HTML template with UTF-8 encoding
    with open("animals_template.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    animal_name = input("Please enter an animal: ")

    # Load animals data from API
    animals_data = data_fetcher.fetch_data(animal_name)

    # Serialize all animals into HTML
    output = ''.join([serialize_animal(animal_obj) for animal_obj in animals_data])

    # Replace the placeholder in the HTML template
    filler_txt = "__REPLACE_ANIMALS_INFO__"
    website_txt = html_content.replace(filler_txt, output)

    # Write the final HTML output to a file with UTF-8 encoding
    with open("animals.html", "w", encoding="utf-8") as file:
        file.write(website_txt)


if __name__ == "__main__":
    main()

import json

with open("Basics\JSON and Python\data.json") as data_file:
    data = json.load(data_file)

for word_data in data["words"]:
    word = word_data["word"]
    examples = word_data["examples"]

    # Print the word itself
    print(f"Word: {word}")

    # Print each example separately
    for example in examples:
        print(f"Example: {example}")

    # Add a separator for better readability
    print("-" * 20)

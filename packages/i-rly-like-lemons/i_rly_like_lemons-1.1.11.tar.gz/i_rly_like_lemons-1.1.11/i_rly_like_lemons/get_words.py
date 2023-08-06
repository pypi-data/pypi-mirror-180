def get_words(words):
    filepath = words
    with open(filepath, "r") as file:
        return file.read()
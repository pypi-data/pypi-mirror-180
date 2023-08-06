def get_words(words):
    filepath = words + ".txt"
    with open(filepath, "r") as file:
        return file.read()
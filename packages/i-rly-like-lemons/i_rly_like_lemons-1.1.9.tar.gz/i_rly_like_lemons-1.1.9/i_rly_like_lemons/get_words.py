def get_words(words):
    filepath = "i_rly_like_lemons/" + words + ".txt"
    with open(filepath, "r") as file:
        return file.read()
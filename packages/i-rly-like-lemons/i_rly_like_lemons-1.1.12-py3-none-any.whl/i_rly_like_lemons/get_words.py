from importlib import resources

def get_words(words):
    with resources.open_text("i_rly_like_lemons", words + ".txt") as file:
        return file.read()
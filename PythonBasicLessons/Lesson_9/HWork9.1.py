#Determining the popularity of certain words in the text
def popular_words (text: str, words: list):
    """
    Determining the popularity of certain words in the text.
    :param text: text with "popular words" in different register
    :param words: "popular words"
    :return: Dictionary with "popular words" as key and the number
    of "popular words" in the text as value

    """
    text = text.lower().split()
    numb_words = []
    for word in words:
        numb_words.append(text.count(word))
    zipped_data = zip(words, numb_words)
    result = list(zipped_data)
    print(dict(result))

popular_words ('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near'])

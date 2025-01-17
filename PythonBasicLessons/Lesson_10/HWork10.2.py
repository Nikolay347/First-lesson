# Find the first word
import re   #Regular expression operations

def first_word(text):
    """
    Search for the first word
    :param text: given expression, str
    :return: first word, which was separated from expression, str
    :conditionals: There may be periods and/or commas in the line
A string can start with a letter or, for example, a space or a period
A word can have an apostrophe and it is part of the word
The entire text can be represented by just one word and that's it
    """
    text = re.split("[,. ]", text)
    for elem in text:
        if elem.isalnum() or "'" in elem:
            text = elem
            break
    return text

first_word("Hello.World")

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')


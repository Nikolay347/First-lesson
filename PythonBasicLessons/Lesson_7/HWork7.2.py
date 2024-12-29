# # To modify the string

def correct_sentence(text):
    s_upper = text[0].upper()
    s_lower = text[1:]
    text = s_upper+s_lower
    if not text.endswith("."):
        text = text + "."
        # print(text)                   #for output variant
    return text

sentence = input("Input sentence: ")
# correct_sentence(sentence)            #for output variant
print(sentence,"==", correct_sentence(sentence))



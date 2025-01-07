## Palindrome
import string
def is_palindrome(text):
    new_text = []
    for i in text:
        if i in string.punctuation or  i == " ":
            continue
        else:
            i = i.lower()
            new_text.append(i)
    new_text1 = new_text[::-1]
    if new_text == new_text1:
        print(True)
    else:
        print(False)

is_palindrome('A man, a plan, a canal: Panama')

#HW 12.1. Clean the text from html tags
import re
import codecs           #This module defines base classes for standard Python codecs (encoders and decoders)
                        # and provides access to the internal Python codec registry, which manages the codec
                        # error handling lookup process. Most standard codecs are text encodings, which encode
                        # text to bytes (and decode bytes to text), but there are also codecs provided that encode
                        # text to text, and bytes to bytes. Custom codecs may encode and decode between arbitrary
                        # types, but some module features are restricted to be used specifically with text encodings
                        # or with codecs that encode to bytes.
def delete_html_tags(html_file, result_file = 'cleaned.txt'):
    '''
    a function that reads a given html file, cleans the text
    from html tags and writes this text to another file.
    :param html_file: file to clean up
    :param result_file: file name where the cleaned text should be written
    :return: file with recorded cleaned text
    '''
    with codecs.open(html_file, 'r', 'utf-8') as html_file:
        result_list = []
        for line in html_file:
            find_text = re.findall(r">([^>]+)<", line)
            if len(find_text) > 0:
                result_list += find_text
        print(f"Result: {result_list}")
        if len(result_list) > 0:
            with open(result_file, 'w', encoding='utf-8') as new_html_file:
                new_html_file.write("\n".join(result_list))
                # new_html_file.write("\n".join(result_list[4:]))   # The same, but removed "empty" (not joking!) lines


delete_html_tags("draft.html")
##############################################################################
#v.2: Same, but different pattern
# import re
# import codecs
# def delete_html_tags(html_file, result_file = 'cleaned.txt'):
#     with codecs.open(html_file, 'r', 'utf-8') as html_file:
#         result_list = []
#         for line in html_file:
#             find_text = re.findall(r">(.+)</", line)
#             if len(find_text) > 0:
#                 result_list += find_text
#         print(f"Result: {result_list}")
#         # if len(result_list) > 0:
#             # with open(result_file, 'w', encoding='utf-8') as new_html_file:
#             #     new_html_file.write("\n".join(result_list))
#
#
# delete_html_tags("draft.html")
#########################################################################################################

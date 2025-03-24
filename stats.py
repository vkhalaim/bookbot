def get_num_words(text):
    num_words = len(text.split())
    return f"Found {num_words} total words"


def get_character_frequency(text):
    res = dict()
    for word in text:
        for char in word.lower():
            if char not in res:
                res[char] = 1
            else:
                res[char] += 1
    return res


def sorted_by_frequency(dictionary):
    sorted_dictionary = sorted(dictionary.items(), key=lambda x:x[1], reverse=True)
    converted_dict = dict(sorted_dictionary)
    return converted_dict

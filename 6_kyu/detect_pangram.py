from string import ascii_lowercase


def is_pangram(s):
    set_of_text = set(s.lower())
    list_of_text = []
    for i in set_of_text:
        if i in ascii_lowercase:
            list_of_text.append(i)
    return True if len(list_of_text) == len(ascii_lowercase) else False

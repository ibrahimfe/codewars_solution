def get_count(sentence):
    a = "aiueo"
    count = 0
    for i in sentence:
        if i in a:
            count += 1
    return count

def duplicate_count(text):
    text = text.lower()
    clean_text = set(text)
    duplicates = 0
    for i in clean_text:
        if text.count(i) > 1:
            duplicates += 1
    return duplicates

def duplicate_count(text):
    text = text.lower()
    set_of_text = set(text)
    count = sum(1 for i in set_of_text if text.count(i) > 1)
    return count

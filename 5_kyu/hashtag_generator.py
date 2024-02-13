def generate_hashtag(s):
    if not s:  # Combine empty check and length check
        return False

    words = s.lower().strip().split()  # Lowercase and split in one step
    hashtag = "#" + "".join(word.title() for word in words)  # Combine operations
    return hashtag if len(hashtag) <= 140 else False

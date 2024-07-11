def merge_strings(str1, str2):
    # Find the longest possible overlap
    max_overlap = 0
    for i in range(1, min(len(str1), len(str2)) + 1):
        if str1[-i:] == str2[:i]:
            max_overlap = i

    # Merge the strings with the overlap
    merged_string = str1 + str2[max_overlap:]
    return merged_string


# Test cases
print(merge_strings("abcde", "cdefgh"))  # Output: "abcdefgh"
print(merge_strings("abaab", "aabab"))  # Output: "abaabab"
print(merge_strings("abc", "def"))  # Output: "abcdef"
print(merge_strings("abc", "abc"))  # Output: "abc"
print(merge_strings("abaabaab", "aabaabab"))  # Output: "abaabaabab"

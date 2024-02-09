def count_smileys(arr):
    count = 0
    for face in arr:
        if ":" == face[0] or ";" == face[0]:
            if "-" == face[1] or "~" == face[1]:
                if ")" in face or "D" in face:
                    count += 1
            elif ")" == face[1] or "D" == face[1]:
                count += 1
    return count

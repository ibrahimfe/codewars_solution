def find_array(arr1, arr2):
    if not arr1 or not arr2:
        return []
    mylist = []
    for i in arr2:
        if i < len(arr1):
            mylist.append(arr1[i])
    return mylist

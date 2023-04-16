def find_smallest_int(arr):
    smallest = arr[0]
    for i in arr:
        if i < smallest:
            smallest = i
    return smallest


# or
#  def find_smallest_int(arr):
#      return min(arr)

# or
# def find_smallest_int(arr):
#     arr.sort()
#     return arr[0]

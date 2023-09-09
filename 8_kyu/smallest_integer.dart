int findSmallestInt(List<int> arr) {
  int smallest_number = arr[0];
  for (int i = 1; i < arr.length; i++) {
    if (arr[i] < smallest_number) {
      smallest_number = arr[i];
    }
  }
  return smallest_number;
}

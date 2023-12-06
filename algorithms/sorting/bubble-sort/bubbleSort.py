def bubbleSort(arr: list[int]) -> list[int]:
  hasSwapped = False
  for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
      if arr[j] > arr[j+1]:
        hasSwapped = True
        arr[j+1], arr[j] = arr[j], arr[j+1]

    if not hasSwapped: # already sorted
      return
  return arr



if __name__ == '__main__':
  a = [1, 2, 3, 5, 4, 6, 9, 8]
  print(a)
  res = bubbleSort(a)
  print(res)
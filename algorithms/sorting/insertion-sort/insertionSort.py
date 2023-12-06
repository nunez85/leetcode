def insertionSort(arr: list[int]) -> list[int]:
  if len(arr) <= 1:
    return arr

  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and key < arr[j]:
      arr[j+1] = arr[j]
      j -= 1 
    arr[j+1] = key

  return arr


if __name__ == '__main__':
  a = [4, 7, 1, 3, 2, 9, 12, 5]
  print(a)
  res = insertionSort(a)
  print(res)
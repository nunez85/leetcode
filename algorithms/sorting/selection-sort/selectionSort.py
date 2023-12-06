def selectionSort(arr: list[int]) -> list[int]:
  for i in range(len(arr)):
    min_index = i

    for j in range(i+1, len(arr)):
      if arr[j] < arr[min_index]:
        min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

  return arr


if __name__ == '__main__':
  a = [4, 7, 1, 3, 2, 9, 12, 5]
  print(a)
  res = selectionSort(a)
  print(res)
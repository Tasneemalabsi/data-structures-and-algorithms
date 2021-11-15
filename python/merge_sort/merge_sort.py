list1 = [8,4,23,16,15,42]

def merge_sort(arr):
    n = len(arr)

    if n > 1:
      mid_point = n//2
      left_part = arr[:mid_point]
      right_part = arr[mid_point:]
      merge_sort(left_part)
      merge_sort(right_part)

      merge(left_part, right_part, arr)
    return arr

def merge(left_part, right_part, arr):
     i = 0
     j = 0
     k = 0

     while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i = i + 1
        else:
            arr[k] = right_part[j]
            j = j + 1

        k = k + 1

     while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

     while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

if __name__ == "__main__":
    print(merge_sort(list1))

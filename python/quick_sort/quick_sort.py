arr = [8,4,23,42,16,15]

def quick_sort(arr, left, right):
    if left < right:

        position = Partition(arr, left, right)
        quick_sort(arr, left, position - 1)
        quick_sort(arr, position + 1, right)
    return arr

def Partition(arr, left, right):
    print("right  ",right)
    pivot = arr[right]
    print("left  ",left)
    low = left - 1
    print("pivot  ",pivot)
    for i in range(left,right):
        if arr[i] <= pivot:
            low += 1
            Swap(arr, i, low)
    Swap(arr, right, low + 1)
    return low + 1

def Swap(arr, i, low):
    temp =  arr[i]
    arr[i] =  arr[low]
    arr[low] =  temp


if __name__ == "__main__":
    print(quick_sort(arr, 0, len(arr)-1))

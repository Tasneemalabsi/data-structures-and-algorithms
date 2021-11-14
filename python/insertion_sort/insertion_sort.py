list1=[8,4,23,42,16,15]

def insertion_sort(arr):
    for i in range(1,len(arr)):
        current = arr[i]
        temp_index =i-1
        while current<arr[temp_index] and temp_index>=0:
            arr[temp_index+ 1] = arr[temp_index]
            temp_index = temp_index -1
        arr[temp_index + 1] = current
    return arr

if __name__ == "__main__":
    print(insertion_sort(list1))

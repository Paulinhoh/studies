# ------------------------------ counting sort ------------------------------------
# cost: O(n)
def counting_sort(arr):
    size = len(arr)
    output = [0] * size

    count = [0] * 10

    for i in range(0, size):
        count[arr[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]

# ------------------------------ quick sort ------------------------------------
# cost: O(n*log(n)) --> pivo aleatorio | O(n²) --> pivo ultimo elemento
def quick_sort(arr, start_pointer=0, end_pointer=None):
    if end_pointer is None:
        end_pointer = len(arr) - 1
    
    if start_pointer < end_pointer:
        index_pivot = partition(arr, start_pointer, end_pointer)
        quick_sort(arr, start_pointer, index_pivot-1)
        quick_sort(arr, index_pivot+1, end_pointer)


def partition(arr, start_pointer, end_pointer):
    pivot = arr[end_pointer]
    i = start_pointer
    
    for j in range(start_pointer, end_pointer):
        if arr[j] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    
    arr[i], arr[end_pointer] = arr[end_pointer], arr[i]
    
    return i


# ------------------------------ merge sort ------------------------------------
# cost: O(n*log(n))
def merge_sort(arr, start_pointer=0, end_pointer=None):
    if end_pointer is None:
        end_pointer = len(arr)
   
    if (end_pointer - start_pointer > 1):
        mid_pointer = (end_pointer + start_pointer) // 2
        merge_sort(arr, start_pointer, mid_pointer)
        merge_sort(arr, mid_pointer, end_pointer)
        merge(arr, start_pointer, mid_pointer, end_pointer)


def merge(arr, start_pointer, mid_pointer, end_pointer):
    left = arr[start_pointer:mid_pointer]
    right = arr[mid_pointer:end_pointer]
    top_left, top_right = 0, 0
    
    for k in range(start_pointer, end_pointer):
        if top_left >= len(left):
            arr[k] = right[top_right]
            top_right += 1
        elif top_right >= len(right):
            arr[k] = left[top_left]
            top_left += 1
        elif left[top_left] < right[top_right]:
            arr[k] = left[top_left]
            top_left += 1
        else:
            arr[k] = right[top_right]
            top_right += 1


# ------------------------------ insertion sort --------------------------------
# cost: O(n²)
def insertion_sort(arr):
    size = len(arr)
    
    for i in range(1, size):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


# ------------------------------ bubble sort -----------------------------------
# cost: O(n²)
def bubble_sort(arr):
    size = len(arr)
    
    for j in range(size-1):
        for i in range(size-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]


# ------------------------------ selection sort --------------------------------
# cost: O(n²)
def selection_sort(arr):
    size = len(arr)
    
    for j in range(size):
        index_min = j
        for i in range(j, size):
            if arr[i] < arr[index_min]:
                index_min = i

        if arr[j] > arr[index_min]:
            arr[j], arr[index_min] = arr[index_min], arr[j]


# ---------------------------- main --------------------------------------------
def main():
    array = [3,9,2,5,1,7]

    quick_sort(array)
    
    print("\nOrdened array:")
    print(array)


if __name__=='__main__':
    main()
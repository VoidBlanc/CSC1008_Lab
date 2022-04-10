def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot+1, high)

def partition(arr, low, high):
    pivot_index = low
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[pivot_index], arr[j] =  arr[j], arr[pivot_index]
            pivot_index += 1

    arr[pivot_index], arr[high] = arr[high] ,arr[pivot_index]
    return pivot_index    
    

if __name__ == "__main__":
    arr = ['E','A', 'S','Y','Q','U','E','S','T','I', 'O','N']
    
    print("------------------\t SELECTION SORT \t------------------")
    quick_sort(arr, 0, len(arr)-1)
    print(arr)

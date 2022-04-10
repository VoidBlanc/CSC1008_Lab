from turtle import right

# Selection Sort
def selection_sort(arr):
    min = 0
    for i in range(len(arr)):
        # Set first index as minimum index
        min = i
        
        # Find minimum value
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[min]):
                min = j
                
        # Swap current and minimum
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp


if __name__ == "__main__":
    arr = ['E','A', 'S','Y','Q','U','E','S','T','I', 'O','N']
    
    print("------------------\t SELECTION SORT \t------------------")
    selection_sort(arr)
    print(arr)

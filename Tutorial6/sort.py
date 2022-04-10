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


def insertion_sort(arr):
    if len(arr) <= 0 :
        print("ERROR")
       
    # Mark first one as sorted    

    for i in range(1, len(arr)):
        current = i
        while current > 0 and arr[current-1] > arr[current]:
            temp = arr[current]
            arr[current] = arr[current-1]
            arr[current-1] = temp
            current -= 1

            


if __name__ == "__main__":
    arr = ['E','A', 'S','Y','Q','U','E','S','T','I', 'O','N']
    selection_sort(arr)
    print("------------------\t SELECTION SORT \t------------------")
    print(arr)
    arr = ['E','A', 'S','Y','Q','U','E','S','T','I', 'O','N']
    insertion_sort(arr)
    print(arr)
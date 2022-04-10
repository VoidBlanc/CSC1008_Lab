# Inserion Sort
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

    print("------------------\t INSERTION SORT \t------------------")
    insertion_sort(arr)

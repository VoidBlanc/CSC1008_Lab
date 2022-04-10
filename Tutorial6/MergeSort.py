# Iterative Merge Sort
def merge_sort(array1, array2):
    arr_combined = []

    # while array1 and array2:
    #     if array1[0] > array2[0]:
    #         arra
    pass

# Recursive Merge Sort
def merge_sort2(arr):
    length = len(arr)
    if length == 1:
        return arr
    
    mid = length//2
    
    array1 = merge_sort2(arr[:mid])
    array2 = merge_sort2(arr[mid:])
    comb =  merge(array1, array2)
    return comb

# Merge Sort Merging
def merge(leftarr, rightarr):
    mergearr = []
    i = j = 0
    
    while i < len(leftarr) and j < len(rightarr):
        if leftarr[i] < rightarr[j]:
            mergearr.append(leftarr[i])
            i += 1
        else:
            mergearr.append(rightarr[j])
            j += 1
            
    while i < len(leftarr):
        mergearr.append(leftarr[i])
        i+=1

    while j < len(rightarr):
        mergearr.append(rightarr[j])
        j+=1
        
    return mergearr


if __name__ == "__main__":
    arr = ['E','A', 'S','Y','Q','U','E','S','T','I', 'O','N']
    
    print("------------------\t MERGE SORT \t------------------")
    new = merge_sort2(arr)
    print(new)
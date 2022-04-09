import random


class BinarySearchST:
    def __init__(self):
        self.data = [1,5,8,9,10]

    # Iterative Search
    def search(self, low, high, searchval):
        if searchval not in self.data:
            return -1
        mid = low  + (high-low)//2
        
        if searchval < self.data[mid]:
            for i in range(0, mid):
                if self.data[i] == searchval:
                    return i
        elif searchval > self.data[mid]:
            for i in range(mid, len(self.data)):
                if self.data[i] == searchval:
                    return i 
        elif searchval == self.data[mid]:
            # If mid  == self.data[mid]
            return mid


    # Recursive Search        
    def search2(self, low, high, searchval):
        if searchval not in self.data:
            return -1
        mid = low  + (high-low)//2
        if searchval == self.data[mid]:
            return mid
        if searchval < self.data[mid]:
            return self.search2(low, mid-1, searchval)
        if searchval > self.data[mid]:
            return self.search2(mid+1, high, searchval)
    

random.seed(1)
dataSize = int(input("Enter the size of the list:\n"))
data = [random.randint(1,dataSize) for i in range(dataSize)]
data.sort()
test = BinarySearchST()
test.data = data
print(test.search(0,len(test.data)-1,9132))
print(test.search2(0,len(test.data)-1,9132))
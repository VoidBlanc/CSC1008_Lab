import math


class BinarySearchST:
    def __init__(self):
        self.data = [1,5,8,9,10]

    # Iterative Search
    def search(self, searchval):
        mid = math.ceil(len(self.data)/2)
        
        if searchval < self.data[mid]:
            for i in range(0, mid):
                if self.data[i] == searchval:
                    return self.data[i]
        elif searchval > self.data[mid]:
            for i in range(mid, len(self.data)):
                if self.data[i] == searchval:
                    return self.data[i] 
        else:
            # If mid  == self.data[mid]
            return searchval

    # Recursive Search        
    def search2(self, mid, searchval):
        if searchval == self.data[mid]:
            return searchval
        
        if searchval < self.data[mid]:
            return self.search2(mid-1, searchval)
        
        if searchval > self.data[mid]:
            return self.search2(mid+1, searchval)

test = BinarySearchST()
mid = math.ceil(len(test.data)/2)
print(test.search(1))
print(test.search2(mid,1))
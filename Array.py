import ctypes 
class MyList:
    
    def __init__(self):
        self.n = 0
        self.size = 1
        self.A = self._make_array(self.size)
        
    def __len__(self):
            return self.n
    
    def __str__(self):
        temp = ""
        
        for i in range(self.n):
            
            temp = temp + str(self.A[i]) + ","
        temp = temp[:-1]
        
        return "[" + temp + "]"
    
    def __getitem__(self, index):
        
        if 0<=index<=self.n:
            return self.A[index]
        else:
            return "Index error"
        
        
    def __delitem__(self, index):
        if 0<=index<=self.n:
            #delete
            for i in range(index, self.n-1):
                self.A[i]=self.A[i+1]
            self.n-=1
                
        else:
            return "Index Error"
        
        
    def remove(self, value):
        flag = 0
        for i in range(self.n):
            if self.A[i]==value:
                flag=1
                for j in range(i, self.n-1):
                    self.A[j]=self.A[j+1]
                self.n-=1
                break
        if flag==0:
            print("Not Found")
    
    def append(self , item):
        
            if self.n == self.size:
                
                self._resize(2 * self.size)
                
            self.A[self.n] = item
            self.n += 1
            
    def insert(self, index, value):
        if 0<=index<=self.n:
            #do the insertion
            if self.n == self.size:
                self._resize(2 * self.size)
                
            for i in range(self.n-1, index-1, -1):
                self.A[i+1]=self.A[i]
                
            self.A[index]=value
            self.n+=1
        else:
            return "Index Error"
        
    def pop(self) :
        self.n-=1
            
        
    def clear(self):
        self.n=0
        self.size=1
        
        
    def find(self, item):
        flag = 0
        for i in range(self.n):
            if self.A[i]==item:
                flag =1
                break
        if flag == 1:
            return i
        else:
            return "Not Found"
                
                
    def _resize(self, new_capacity):
            #1 create array
            B = self._make_array(new_capacity)
            self.size = new_capacity 
            #2 copy
            for i in range(self.n):
                B[i] = self.A[i]
            #3 Reassign
            self.A = B 
            self.size = new_capacity
    def _make_array(self, capacity) :
        return (capacity * ctypes.py_object)()

    
arr = MyList()
# arr.append(1)
# arr.append(2)
# arr.append(5)
# print(len(arr))
# print(arr[0])
# arr.insert(2,100)
# del arr[2]
# print(arr)

# #remove
# arr.append(1)
# arr.append(100)
# arr.remove(1000)
# print(arr)

#pop
# arr.append(10)
# arr.append(30)
# arr.pop()
# print(arr)

#clear
# arr.append(10)
# arr.append(30)
# arr.clear()
# print(arr)

#search
arr.append(10)
arr.append(30)
arr.find(100)

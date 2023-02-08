#linear search

def ls(arr):
    n=len(arr)
    for i in range(n):
        if arr[i]==key:
            return i
        
    return -1
            


arr=[5,4,3,2,1,6,7,8,9,10]

key=int(input("enter the key: "))
r=ls(arr)
if r==-1:
    print("element not found")
else:
    print("found at index: ",r)





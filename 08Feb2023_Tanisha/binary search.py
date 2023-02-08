#binary search

def bs(arr):
    low=0
    high=len(arr)-1
    mid=0
    
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<key:
            low=mid+1
        elif arr[mid]>key:
            high=mid-1
        else:
            return mid
    else:
       return -1


        
        
    
arr=[5,4,3,2,1,6,7,8,9,10]
arr1=sorted(arr)
key=int(input("enter a key: "))
r=bs(arr1)
if r==-1:
    print("element not present")
else:
    print("element present at index",r)

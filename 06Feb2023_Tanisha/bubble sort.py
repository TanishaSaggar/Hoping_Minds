#bubble sort 


#for ascending order
def asc(arr):
    n=len(arr)
    swapped=False
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                swapped=True
                arr[j],arr[j+1]=arr[j+1],arr[j]
                print(arr)
                if not swapped:
                    return

def desc(arr):
    n=len(arr)
    swapped=False
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]<arr[j+1]:
                swapped=True
                arr[j],arr[j+1]=arr[j+1],arr[j]
                print(arr)
                if not swapped:
                    return    
            
arr=[1,9,7,4,10,5]
v=int(input("enter input 1 for ascc and 2 for dec : "))
if v==1:
    asc(arr)
else:
    desc(arr)
    
"""d=int(input("enter length of array:"))
for p in range(d):
    arr=int(input("enter another element"))
v=int(input("enter input 1 for ascc and 2 for dec"))
if v==1:
    asc(arr)
else:
    desc(arr)"""

    

 
print("Sorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")
    
    




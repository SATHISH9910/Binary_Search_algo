arr=[10,22,33,40,50,66]
target=34
low=0
high=len(arr)-1
floor=None
ciel=None
while low<=high :
    mid=(low+high)//2
    if arr[mid]==target:
        floor=arr[mid]
        ciel=arr[mid]
        break
    elif target>arr[mid]:
        floor=arr[mid]
        low=mid+1
    else:
        ciel=arr[mid]
        high=mid-1
print("Floor =",floor)
print("Ciel",ciel)

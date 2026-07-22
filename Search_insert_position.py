arr=[10,20,30,40,50]
target=35
low=0
high=len(arr)-1
found=False
while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
        found=True
        print("Element found at index",mid)

    elif target>arr[mid]:
        low=mid+1
    else:
        high=mid-1
if not found:
    print("Insertion position is",low)

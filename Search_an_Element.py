arr = [10, 20, 30, 40, 50, 60, 70]
target = 40

# Starting index
low = 0

# Last index
high = len(arr) - 1

# Repeat until search space is empty
while low <= high:

    # Find the middle index
    mid = (low + high) // 2

    # Element found
    if arr[mid] == target:
        print("Element found at index", mid)
        break

    # Search in the right half
    elif target > arr[mid]:
        low = mid + 1

    # Search in the left half
    else:
        high = mid - 1
else:
    # Element not found
    print("Element not found")

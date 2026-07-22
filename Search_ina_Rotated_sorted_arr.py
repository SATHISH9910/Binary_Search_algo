# Rotated sorted array
arr = [30, 40, 50, 60, 25, 15, 5]

# Element to search
target = 15

# Starting and ending indexes
low = 0
high = len(arr) - 1

# Repeat until search space is empty
while low <= high:

    # Find the middle index
    mid = (low + high) // 2

    # Target found
    if arr[mid] == target:
        print("Element found at index", mid)
        break

    # Check if the left half is sorted
    elif arr[low] <= arr[mid]:

        # Is the target in the left half?
        if arr[low] <= target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    # Otherwise, the right half is sorted
    else:

        # Is the target in the right half?
        if arr[mid] < target <= arr[high]:
            low = mid + 1
        else:
            high = mid - 1

# Executed only if the loop finishes without break
else:
    print("Element not found")
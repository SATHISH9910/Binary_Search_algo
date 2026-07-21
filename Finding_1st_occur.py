arr = [10, 20, 20, 20, 30, 40]
target = 20

# Starting index
low = 0

# Last index
high = len(arr) - 1

# Stores the first occurrence index
answer = -1

# Repeat until search space is empty
while low <= high:

    # Find the middle index
    mid = (low + high) // 2

    # Target found
    if arr[mid] == target:

        # Store current index
        answer = mid

        # Search left side for an earlier occurrence
        high = mid - 1

    # Search right half
    elif target > arr[mid]:
        low = mid + 1

    # Search left half
    else:
        high = mid - 1

# Check if target was found
if answer == -1:
    print("Element not found")
else:
    print("First occurrence is at index", answer)
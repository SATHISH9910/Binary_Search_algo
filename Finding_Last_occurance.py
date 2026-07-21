# Sorted array
arr = [10, 20, 20, 20, 30, 40]

# Element to search
target = 20

# Starting index
low = 0

# Last index
high = len(arr) - 1

# Stores the last occurrence index
answer = -1

# Repeat until the search space becomes empty
while low <= high:

    # Find the middle index
    mid = (low + high) // 2

    # Target found
    if arr[mid] == target:

        # Store the current index
        answer = mid

        # Search the right side for the last occurrence
        low = mid + 1

    # Target is greater than middle element
    elif target > arr[mid]:

        # Move to the right half
        low = mid + 1

    # Target is smaller than middle element
    else:

        # Move to the left half
        high = mid - 1

# Check if the element was found
if answer == -1:
    print("Element not found")
else:
    print("Last occurrence is at index", answer)
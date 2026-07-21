# Sorted array
arr = [10, 20, 20, 20, 30, 40]

# Element to search
target = 20

# ---------- Find First Occurrence ----------
low = 0
high = len(arr) - 1
first = -1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        first = mid              # Store first occurrence
        high = mid - 1           # Search left side

    elif target > arr[mid]:
        low = mid + 1            # Search right side

    else:
        high = mid - 1           # Search left side

# ---------- Find Last Occurrence ----------
low = 0
high = len(arr) - 1
last = -1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        last = mid               # Store last occurrence
        low = mid + 1            # Search right side

    elif target > arr[mid]:
        low = mid + 1            # Search right side

    else:
        high = mid - 1           # Search left side

# ---------- Count Total Occurrences ----------
if first == -1:
    print("Element not found")
else:
    count = last - first + 1
    print("First occurrence :", first)
    print("Last occurrence  :", last)
    print("Total occurrences:", count)
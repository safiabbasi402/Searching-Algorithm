def linear_search(arr, target):
    # Linear Search Implementation.
    steps = 0
    for i in range(len(arr)):
        steps = steps + 1
        if arr[i] == target:
            print("Linear Search: Target found at index ", i , " Steps taken: ", steps)
            return
    print("Linear Search: Target not found. Steps taken: ",steps)
    return


def binary_search(arr, target):
    # Binary Search Implementation.
    steps = 0
    first = 0
    last = len(arr) - 1
    while first <= last:
        steps = steps + 1
        mid = (first + last) // 2
        if arr[mid] == target:
            print("Binary Search: Target found at index " , mid, " Steps taken: ",steps)
            return
        elif arr[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    print("Binary Search: Target not found. Steps taken: ",steps)
    return



print("Welcome to Search Algorithms Comparison")
    
# Input array and target
n = int(input("Enter the number of elements you want to add in array: "))
arr = []
for i in range(n):
    elementcount = i + 1
    element = int(input(f"Enter element {elementcount} : " ))
    arr.append(element)


target = int(input("Enter the target number: "))

print("\n    --- Results ---")

# Perform Linear Search
print("Performing Linear Search...")
linear_search(arr, target)
    
# Perform Binary Search
print("\nPerforming Binary Search...")
binary_search(arr, target)
    
# Print time complexities
print("\n--- Time Complexity ---")
print("Linear Search: O(n) (worst case)")
print("Binary Search: O(log n) (worst case)")

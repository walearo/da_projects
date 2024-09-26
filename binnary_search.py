def binary_search(sorted_list, target):
    
    left, right = 0, len(sorted_list) - 1
    
    while left <= right:
        # Find the middle index
        mid = (left + right) // 2
        
        # Check if the target is at mid
        if sorted_list[mid] == target:
            return mid  # Target found, return index
        # If target is greater, ignore the left half
        elif sorted_list[mid] < target:
            left = mid + 1
        # If target is smaller, ignore the right half
        else:
            right = mid - 1
    
    # Target not found
    return -1
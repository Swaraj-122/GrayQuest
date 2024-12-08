def find_pair_with_sum(arr, target):
    n = len(arr)
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            pivot = i
            break
    else:
        pivot = -1


    left = (pivot + 1) % n  
    right = pivot           

    while left != right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return True  
        elif current_sum < target:
            left = (left + 1) % n
        else:
            right = (right - 1 + n) % n
    
    return False



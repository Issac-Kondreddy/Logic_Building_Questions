def swap(arr, start1, start2, size):
    for i in range(size):
        arr[start1 + i], arr[start2 + i] = arr[start2 + i], arr[start1 + i]

def recursive_block_swap(arr, start_a, start_b, size_a, size_b):
    if size_a == 0 or size_b == 0:
        return

    # If the segments are of equal size, swap them and we're done
    if size_a == size_b:
        swap(arr, start_a, start_b, size_a)
        return

    # If the first segment is smaller, swap it with the first part of the second segment
    if size_a < size_b:
        swap(arr, start_a, start_b, size_a)
        recursive_block_swap(arr, start_a, start_b + size_a, size_a, size_b - size_a)
    else:
        # If the second segment is smaller, swap it with the last part of the first segment
        swap(arr, start_a, start_b, size_b)
        recursive_block_swap(arr, start_a + size_b, start_b, size_a - size_b, size_b)

def block_swap_rotate(arr, n, d):
    if d == 0 or d == n:
        return arr
    d = d % n
    recursive_block_swap(arr, 0, d, d, n - d)
    return arr

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8]
d = 3
print("Before rotation:", arr)
print("After rotation:", block_swap_rotate(arr, len(arr), d))

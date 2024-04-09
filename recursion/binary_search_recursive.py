# Binary search using recursion
def binary_search_recursive(L, left, right, x):
    if left > right:
        return -1
    
    mid = (left + right) // 2

    if L[mid] == x:
        return mid
    elif L[mid] < x:
        return binary_search_recursive(L, mid + 1, right, x)
    else:
        return binary_search_recursive(L, left, mid - 1, x)
    

# Test the binary search
if __name__ == '__main__':
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # List must be sorted
    left = 0
    right = len(L) - 1

    for x in range(1, 12):
        position = binary_search_recursive(L, left, right, x)

        if position == -1:
            if x in L:
                print('Error: Binary search is not working properly')
            else:
                print('Element not found')

        else:
            if L[position] == x:
                print('Element found at position', position)
            else:
                print('Error: Binary search is not working properly')

    print("program Terminated...")
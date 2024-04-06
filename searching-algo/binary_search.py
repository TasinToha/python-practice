def binary_search(L, x):
    left, right = 0, len(L)-1

    while left <= right:
        mid = (left + right) // 2

        if L[mid] == x:
            return mid
        elif L[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Test the binary_search function
if __name__ == "__main__":
    L = [1, 2, 4, 6, 9]

    for x in range(1, 11):
        position = binary_search(L, x)

        if position == -1:
            if x in L:
                print(x, "is in L, but function returned -1")
            else:
                print(x, "not in list")

        else:
            if L[position] == x:
                print(x, "found at position", position)
            else:
                print("Binary search returned", position, "for", x, "which is", L[position])

    print("Program terminated")
def selecton_sort(L):
    n = len(L)

    for i in range(0, n-1):
        min_index = i

        for j in range(i+1, n):
            if L[j] < L[min_index]:
                min_index = j

        if min_index != i:
            L[i], L[min_index] = L[min_index], L[i]


if __name__ == "__main__":
    L = [6, 1, 4, 9, 2]
    print("Before sort:", L)
    selecton_sort(L)
    print("After sort:", L)
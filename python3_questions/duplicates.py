# Write a function that finds the duplicate items in any given array
# Python 3 code to find duplicates

def duplicates(arr):
    _size = len(arr)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if arr[i] == arr[j] and arr[i] not in repeated:
                repeated.append(arr[i])
    return repeated

if __name__ == "__main__":
    list2 = [12, 11, 40, 12, 5, 6, 5, 12, 11]
    print (duplicates(list2))


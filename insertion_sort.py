import timeit

def insertion_sort(arr):
    #Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key at the correct position
        arr[j + 1] = key


if __name__ == "__main__":
    data = [12, 11, 13, 5, 6]

    # Make a copy of the data for timeit to ensure it remains unchanged between runs
    data_copy = data.copy()

    #Measure the execution time using timeit
    execution_time = timeit.timeit(stmt="insertion_sort(data_copy)",
                                   setup="from __main__ import insertion_sort, data_copy",
                                   number=1000
                                   )
    print("Original array: ", data)
    insertion_sort(data)
    print("Sorted array: ", data)

    print(f"Execution Time over 1000 runs: {execution_time:.6f}  seconds")
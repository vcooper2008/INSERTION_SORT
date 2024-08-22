import timeit
import tracemalloc

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

# Function to measure execution time
def measure_execution_time(sort_function, data, repetitions):
    data_copy = data.copy()
    statement = sort_function.__name__ + "(data_copy)"
    set_up = "from __main__ import " + sort_function.__name__ +", data_copy"
    execution_time = timeit.timeit(stmt=statement,
                                   setup=set_up,
                                   number=repetitions
                                   )
    return execution_time

# Function to measure memory usage
def measure_memory_usage(sort_function, data):
    data_copy = data.copy()
    tracemalloc.start()
    sort_function(data_copy)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return current, peak

if __name__ == "__main__":
    data = [12, 11, 13, 5, 6]

    # Make a copy of the data for timeit to ensure it remains unchanged between runs
    data_copy = data.copy()

    #Measure the execution time using timeit
    repetitions = 1000
    exec_time = measure_execution_time(insertion_sort, data, repetitions)

    #Measure memory usage
    current_memory, peak_memory = measure_memory_usage(insertion_sort, data)

    # Print results
    print("Original array: ", data)
    insertion_sort(data.copy())
    print("Sorted array: ", data)

    print(f"Execution Time over {repetitions} runs: {exec_time:.6f}  seconds")
    print(f"Current Memory Usage: {current_memory / 10**6:.6f} MB")
    print(f"Peak Memory Usage: {peak_memory / 10**6:.6f} MB")
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Part 1 solution
# Create 2 arrays and quick sort them
# Calculate the sum of the absolute difference between the elements of the 2 arrays
def process_input(data):
    total_sum = 0
    array1 = []
    array2 = []
    for line in data:
        numbers = line.split()
        array1.append(int(numbers[0]))
        array2.append(int(numbers[1]))

    array1 = quicksort(array1)
    array2 = quicksort(array2)

    for i in range(len(array1)):
        total_sum += abs(array1[i] - array2[i])

    print(total_sum)

# Part 2 solution
# Create 2 arrays and calculate the sum of the product of the elements of the 2 arrays
def process_input2(data):
    total_sum = 0
    array1 = []
    array2 = []
    for line in data:
        numbers = line.split()
        array1.append(int(numbers[0]))
        array2.append(int(numbers[1]))

    for num in array1:
        count_in_array2 = array2.count(num)
        total_sum += num * count_in_array2

    print(total_sum)
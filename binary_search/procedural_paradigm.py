def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # Искомый элемент найден, возвращаем индекс
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Искомый элемент не найден

# Пример использования:
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_number = 8

result = binary_search(sorted_array, target_number)

if result != -1:
    print(f"Искомый элемент {target_number} найден в массиве, индекс: {result}")
else:
    print(f"Искомый элемент {target_number} отсутствует в массиве.")

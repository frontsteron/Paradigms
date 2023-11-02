def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


numbers = [4, 2, 9, 1, 5]
sort_list_imperative(numbers)
print(numbers)  # Выведет [9, 5, 4, 2, 1]

def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)


numbers = [4, 2, 9, 1, 5]
sorted_numbers = sort_list_declarative(numbers)
print(sorted_numbers)  # Выведет [9, 5, 4, 2, 1]

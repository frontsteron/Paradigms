from math import sqrt

def mean(values):
    return sum(values) / len(values)

def pearson_correlation(x, y):
    mean_x, mean_y = mean(x), mean(y)
    diff_x = map(lambda xi: xi - mean_x, x)
    diff_y = map(lambda yi: yi - mean_y, y)

    numerator = sum(map(lambda xi, yi: xi * yi, diff_x, diff_y))
    denominator = sqrt(sum(map(lambda xi: xi ** 2, diff_x))) * sqrt(sum(map(lambda yi: yi ** 2, diff_y)))

    if denominator == 0:
        return 0
    else:
        return numerator / denominator

# Пример использования:
array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]

correlation = pearson_correlation(array1, array2)
print(f"Корреляция Пирсона: {correlation}")
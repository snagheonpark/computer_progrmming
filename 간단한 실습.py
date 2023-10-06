numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

results = []

for row in numbers:
    for num in row:
        if num % 2 == 0:
           results.append(num)

print(results)

def add_numbers(a, b):
    result = a + b
    return result

sum_result = add_numbers(5, 3)
print("합계:", sum_result)



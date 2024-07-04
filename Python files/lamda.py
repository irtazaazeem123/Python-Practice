
add_ten = lambda x: x + 10
print(f"Add 10 to 5: {add_ten(5)}")

multiply = lambda x, y: x * y
print(f"Multiply 4 and 5: {multiply(4, 5)}")

# 3. Lambda Function within a List
# A list of tuples with lambda function to sort by the second element
points = [(1, 2), (4, 1), (5, 3), (2, 0)]
sorted_points = sorted(points, key=lambda point: point[1])
print(f"Sorted points by second element: {sorted_points}")

# 4. Using Lambda Function with map()
# A lambda function to square each element in the list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared_numbers}")

# 5. Using Lambda Function with filter()
# A lambda function to filter out even numbers from the list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# 6. Using Lambda Function with reduce()
from functools import reduce

# A lambda function to find

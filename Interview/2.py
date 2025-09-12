# Different Data Types in Python

# 1. Numeric Types
age = 25                        # Integer
pi = 3.14                       # Float
num = 2 + 3j                    # Complex number

# 2. String
name = "Python"

# 3. Boolean
is_active = True

# 4. Sequence Types
fruits = ["apple", "banana", "cherry"]   # List
numbers = (1, 2, 3)                      # Tuple
r = range(5)                             # Range

# 5. Set Types
colors = {"red", "green", "blue"}        # Set
frozen = frozenset(["a", "b", "c"])      # Frozen set

# 6. Mapping Type
student = {"name": "Ankit", "age": 21, "course": "Python"}  # Dictionary

# 7. None Type
x = None

# Print all with their types
print("Integer:", age, type(age))
print("Float:", pi, type(pi))
print("Complex:", num, type(num))
print("String:", name, type(name))
print("Boolean:", is_active, type(is_active))
print("List:", fruits, type(fruits))
print("Tuple:", numbers, type(numbers))
print("Range:", list(r), type(r))
print("Set:", colors, type(colors))
print("Frozen Set:", frozen, type(frozen))
print("Dictionary:", student, type(student))
print("None Type:", x, type(x))

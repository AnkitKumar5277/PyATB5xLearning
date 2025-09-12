
# Python ka simple demo program
age = 21         # integer

# 1. Print something
print("Hello, Welcome to Python!")

# 2. Variables and Dynamic Typing
name = "Ankit"   # string
height = 5.9     # floata

print("My name is:", name)
print("My age is:", age)
print("My height is:", height)

# 3. Conditional statement
if age >= 18:
    print("You are an Adult.")
else:
    print("You are Young.")

# 4. Loop example
for i in range(1, 6):
    print("Number:", i)

# 5. Function example
def greet(user):
    return "Hello " + user + ", welcome to Python!"

print(greet(name))


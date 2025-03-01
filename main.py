# String Formatting
# Use the website PyFormat.info

name = "Hansaka"

age = 18

mg = "Hello %s. Your age is %.2f " % (name , age)

print(mg)

# Using Space Padding
mg = "Hello %s. Your age is %06d " % (name , age)

print(mg)

# Using  Curly Brackets
mg = "Hello {}. Your age is {}" .format(name , age)

print(mg)

# F string formatting
mg = f"Hello {name}. Your age is {age}"

print(mg)
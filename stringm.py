# String manipulation examples

# 1. Concatenation
string1 = "Hello"
string2 = "World"
result = string1 + " " + string2
print("Concatenation:", result)

# 2. Uppercase and Lowercase
string3 = "Python Programming"
print("Uppercase:", string3.upper())
print("Lowercase:", string3.lower())

# 3. Replace characters in a string
string4 = "I like Python"
new_string = string4.replace("like", "love")
print("Replaced string:", new_string)

# 4. Split a string into a list
string5 = "apple,banana,orange"
fruits = string5.split(",")
print("Split string into list:", fruits)

# 5. Joining list into a string
joined_string = " ".join(fruits)
print("Joined list into string:", joined_string)

# 6. Check if a string starts with or ends with a substring
string6 = "Data Science is fun"
print("Starts with 'Data':", string6.startswith("Data"))
print("Ends with 'fun':", string6.endswith("fun"))

# 7. String slicing
string7 = "abcdefg"
print("Slice (first 3 characters):", string7[:3])
print("Slice (last 3 characters):", string7[-3:])

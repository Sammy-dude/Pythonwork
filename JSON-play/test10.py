def complicated_function(x,y,*args):
    print (x,y,args)

complicated_function (x=21,y=20)

a=[10,1,2,3,4,5,10]
print (a)
for i in a:
    print(a)
for x in range(a.__len__()):
    print(a[x])
name ="jum"
age=33
print("my name is", name, "my age is ", age)

print(f"my name :  {name} my age :  {age}")


name = "Jim"
age = 33

# 1. Using concatenation (+)
print("Name: " + name + ", Age: " + str(age))

# 2. Using commas (,)
print("Name:", name, "Age:", age)

# 3. Using str.format()
print("Name: {}, Age: {}".format(name, age))

# 4. Using f-strings (formatted string literals)
print(f"Name: {name}, Age: {age}")

# 5. Using the % operator
print("Name: %s, Age: %d" % (name, age))

# 6. Using locals() with str.format()
print("Name: {name}, Age: {age}".format(**locals()))

# 7. Using repr() for detailed representation
print(f"Name: {repr(name)}, Age: {repr(age)}")

# 8. Using a dictionary with format_map
print("Name: {name}, Age: {age}".format_map({'name': name, 'age': age}))
print("------"*30)
print("Name: {name}, Age: {age}".format_map({'name': name, 'age': age}))
print("------"*30)
print("Name: {name}, Age: {age}".format(**locals()))
print("Name %s, Age: %d" % (name, age))





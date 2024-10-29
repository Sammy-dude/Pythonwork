my_dict = {"name": "Alice", "age": 30, "city": "Boston"}
print("here is  way of priting the whole thing  print(my_dict)   "+("----- "*30))
print(my_dict)
print("here is  way of getting result using regulat   "+("----- "*30))
name = my_dict["name"]  # Access by key
print("name " + name)  # Output: Alice
print("age " + str(my_dict["age"]) ) # Output: Alice
print("city " + my_dict["city"])
print("here is another way of getting result using get  "+("----- "*30))
print("name " + my_dict.get("name"))  # Output: Alice
print("age " + str(my_dict.get("age") )) # Output: Alice
print("city " + my_dict.get("city"))
print("here is another way of getting result using a for loop "+("----- "*30))
print(my_dict.get("city"))
for value in my_dict.values():
      print(value)

print("here is another way of getting result using a for loop "+("----- "*30))
#my_dict = {"name": "Alice", "age": 30, "city": "Boston"}
for key, value in my_dict.items():
      print(f"{key}: {value}")

print("here is another way of getting result using a for second loop "+("----- "*30))
for key1, value1 in my_dict.items():
        print(f"{key1}: {value1}")
        for key2, value2 in my_dict.items():
            print("{key2}: {value2}")





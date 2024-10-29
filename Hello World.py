print("Hello World")


# Function to multiply two numbers

def multiply_string(string1, string2):
    return string1 + string1

# Main program
if __name__ == "__main__":
    # Input first number
    string1 = input("Enter the first string: ")

    # Input second number
    string2 = input("Enter the first string: ")

    # Calculate the product
    product1 = multiply_string(string1, string1)

    # Print the result
    print(f"The joint string of is {product1}")


    # Example of using some reserved keywords
    def example_function():
        for i in range(5):
            if i == 3:
                continue
            elif i == 4:
                break
            else:
                print(i)
        return None


    example_function()





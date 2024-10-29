from this import s


def string_manipulations(s1, s2):
    # Concatenation
    concatenated = s1 + " " + s2
    print(f"Concatenated: {concatenated}")



    # Slicing
    sliced = concatenated[5:15]
    print(f"Sliced: {sliced}")

    # Upper case conversion
    upper_case = concatenated.upper()
    print(f"Upper Case: {upper_case}")

    # Lower case conversion
    lower_case = concatenated.lower()
    print(f"Lower Case: {lower_case}")

    # Reversing
    reversed_string = concatenated[::-1]
   # s2= reverse_stringousama
    print(f"Reversed: {reversed_string}")
    print(f"Reversed2: {s2}")


    # Finding substrings
    find_substring = "string"
    position = concatenated.find(find_substring)
    if position != -1:
        print(f"Substring '{find_substring}' found at position: {position}")
    else:
        print(f"Substring '{find_substring}' not found.")

    # Replacing substrings
    replace_string = "manipulations"
    replaced = concatenated.replace("strings", replace_string)
    print(f"Replaced: {replaced}")

    # Removing whitespace
    with_whitespace = "   Hello World   "
    stripped = with_whitespace.strip()
    print(f"Stripped: '{stripped}'")


# Example usage
s1 = "This is a"
s2 = " string manipulation example"
string_manipulations(s1, s2)


def reverse_string(s):
    return ''.join(reversed(s))

    # Example usage


original_string = s1 + s2
reversed_string = reverse_string(original_string)
print(f"Original: {original_string}")
print(f"Reversed: {reversed_string}")

reverse_string(s)


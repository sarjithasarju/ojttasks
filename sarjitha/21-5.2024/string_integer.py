def string_to_integer(s):
    
    try:
        integer_value = int(s)
        return integer_value
    except ValueError:
        print(f"Error: Unable to convert '{s}' to an integer.")


string = "123"
integer_value = string_to_integer(string)
if integer_value is not None:
    print(f"Integer value of '{string}': {integer_value}")


invalid_string = "abc"
integer_value = string_to_integer(invalid_string)
if integer_value is not None:  
    print(f"Integer value of '{invalid_string}': {integer_value}")
else:
    print(f"Conversion of '{invalid_string}' failed.")

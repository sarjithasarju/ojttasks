def reverse_list(input_list):
    
    reversed_list = input_list[::-1]
    return reversed_list


original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print(f"Original list: {original_list}")
print(f"Reversed list: {reversed_list}")

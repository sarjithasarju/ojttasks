
def remove_element_by_value(input_list, value_to_remove):
    try:
      
        input_list.remove(value_to_remove)
        print(f"Value '{value_to_remove}' removed from the list.")
    except ValueError:
        
        print(f"Value '{value_to_remove}' not found in the list.")


my_list = [1, 2, 3, 4, 5, 6]


value = 3


remove_element_by_value(my_list, value)


print("Updated list:", my_list)

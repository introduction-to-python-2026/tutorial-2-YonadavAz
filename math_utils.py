def find_max_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
         my_max_number = num1  # Replace 'pass' with code
    if num2 >= num1 and num2 >= num3:
        my_max_number = num2
    if num3 >= num1 and num3 >= num2:
        my_max_number = num3
    return my_max_number

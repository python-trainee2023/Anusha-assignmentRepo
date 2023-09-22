# user_input=input("Enter multiple values seperated by a comma: ")
# values=user_input.split(",")

# int_list=[int(x) for x in values if type(x) is int]
# float_list=[float(y) for y in values if type(y) is float]
# string_list=[z for z in values if type(z) is str]

# print("Integer list: ", int_list)
# print("Float list: ", float_list)
# print("String list: ", string_list)


# user_input = input("Enter multiple values seperated by a comma: ")

# values = user_input.split(",")

# int_list = []

# float_list = []

# string_list = []

# for value in values:

#     try:
#         int_value = int(value)
#         int_list.append(int_value)
#     except ValueError:

#         try:
#             float_value = float(value)
#             float_list.append(float_value)
#         except ValueError:
         
#             string_list.append(value)

# print("Integer list: ", int_list)

# print("Float list: ", float_list)

# print("String list: ", string_list)

#to find cube
num=int(input("Enter any number: "))
def cube(num):
    return num**3

print(f"The cube of {num} is {cube(num)}.")

#ask user to ask kati ota term samma ko fibonaci series chainxa and display fibonacci series
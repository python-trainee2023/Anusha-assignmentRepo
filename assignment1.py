user_input=input("Enter multiple values seperated by a comma: ")
values=user_input.split(",")

int_list=[x for x in values if type(x) == int]
float_list=[y for y in values if type(y) == float]
string_list=[z for z in values if type(z) == str]

print("Integer list: ", int_list)
print("Float list: ", float_list)
print("String list: ", string_list)

# my_list = []
# for i in range(20):
#     response = float(input("Please enter a number.\n"))
#     my_list.append(response)
#
# if len(my_list) == 0:
#     exit()
# elif len(my_list) != 0:
#     average = sum(my_list) / len(my_list)
#     print(f"The average is {average}")

def mangle(string):
    upper_case = string.upper()
    remove_third = upper_case[:2]+upper_case[3:]
    remove_third_to_last = remove_third[:-3]+remove_third[-2:]
    print(remove_third_to_last)


mangle("hellothere")
mangle("42 degrees Celsius")
mangle("eeeeeee")

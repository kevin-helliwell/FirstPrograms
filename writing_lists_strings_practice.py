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


# mangle("hellothere")
# mangle("42 degrees Celsius")
# mangle("eeeeeee")

def count_e(list_of_strings):
    total_list = []
    for i in range(len(list_of_strings)):
        total_list += list_of_strings[i]
        print(total_list)
    count = total_list.count("e")+total_list.count("E")
    return count


print(count_e(["hi", "hello", "EEK!"]))
print(count_e(["Eevee", "ELITE", "economy!"]))
print(count_e(["advErtisemEnt", "cosmEtic", "ethics!"]))





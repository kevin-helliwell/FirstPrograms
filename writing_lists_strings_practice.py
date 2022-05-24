my_list = []
for i in range(20):
    response = float(input("Please enter a number.\n"))
    my_list.append(response)

if len(my_list) == 0:
    exit()
elif len(my_list) != 0:
    average = sum(my_list) / len(my_list)
    print(f"The average is {average}")

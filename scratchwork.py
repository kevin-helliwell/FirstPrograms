# string = "hello"
# length = 0
# for char in string:
#     length += 1
# print(string, "length is", length)
#
#
# mmm = 4
# for i in range(10):
#     if i % 3 == 0:
#         mmm += i
# print(mmm)
#
#
# list = [2, 6, -3, 5]
# total = 0
# for x in list:
#     if x > 0:
#         total = total + x
# print(total)

# x = 0
# for j in range(-5, 6):
#     if j >= 0:
#         if j % 2 == 0:
#             x += j
#         else:
#             x -= j
#     else:
#         if j % 5 == 0:
#             x *= -1 * j
#         x += j
#     print(x)
# print(x)

# list = []
# i = 0
# count = 0
#
# response = input("Enter a number (Press Q to quit.)?")
# list.append(response)
# # count += list[0].count("0")
#
# while response != "Q":
#     response = input("Enter a number (Press Q to quit.)?")
#     list.append(response)
#     count += list[i].count("0")
#     i += 1
# else:
#     print(f"You entered {count} zeroes")

# def count_fricatives(list_of_strings):
#     fricative_list = ["f", "s", "v", "z"]
#     total_list = []
#     i = 0
#     j = 0
#     count = 0
#     while i < len(list_of_strings):
#         total_list += list_of_strings[i].lower()
#         i += 1
#     while j < len(fricative_list):
#         count += total_list.count(fricative_list[j])
#         j += 1
#
#     return count


# list = ["Zebra", "lightsaber", "1234 JOYS!"]
# print(count_fricatives(list))


# def well(x):
#     t = -3
#     while t < x:
#         if t < 0:
#             t += x
#         else:
#             t *= 2
#     return t


# print(well(5))

def why11(list):
    y = 1
    j = 0
    while j < len(list) and y < 11:
        x = list[j]
        if x < 0:
            y-= x
        elif x % 2 == 0:
            y *= x
        else:
            y += x
        j += 2
    return y


# print(why11([4, -1, -5, 2, 1, 3, 7, -8]))
#
# phrase = "Happy Summer!"
# print(phrase[1])
# print(phrase[-7])
# print(phrase[-4:])
# print(phrase[3:8])
#
# list = ["Rose City", "Dodgers", "Madison", "NJ"]
# print(list[2], list[-2], list[:2])
#
# def find_u(string):
#     letter_list = []
#     for letter in string:
#         letter_list.append(letter.lower())
#         # print(letter_list)
#         count = letter_list.count("u")
#     if count > 0:
#         return letter_list.index("u")
#     else:
#         return -1
#
#
# print(find_u("OUCH"))
# print(find_u("oops"))

def average_vowels(list_of_strings):
    i = 0
    num = 0
    total = 0
    vowel_list = ["a", "o", "i", "u", "e"]
    while i < len(list_of_strings):
        string = list_of_strings[i].lower()
        for vowel in vowel_list:
            if vowel in string:
                total += 1
        i += 1
    return total/i


list = ["Zebra", "lightsaber", "1234 JOYS!"]
print(average_vowels(list))

# string = "hello"
# string[2] = "y"
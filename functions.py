def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def calculate_total(meal, tax_rate, tip_rate):
    total = meal*(1+tax_rate+tip_rate)
    return total


def hey(number):
    return number**2


def there(n):
    if n >= 0:
        return 2**n
    else:
        return 0


def are_we(number, phrase):
    string = (number*f"Are we {phrase} yet? ")
    return string


# print(is_even(50), is_even(101))
# print(calculate_total(53.48, 0.07, 0.18))
# print(hey(5), hey(0), hey(-3))
# print(there(5), there(0), there(3), there(-2), there(-6))
# print(are_we(2, "there"))
# print(are_we(3, "50"))
# print(are_we(1, ""))
# print(are_we(0, "hey!"))

def what(num):
    tip = -3
    for i in range(num):
        tip += i
    return tip


def rectangle(width, height):
    for i in range(height):
        print(width*"*")


print(what(5))
rectangle(5, 3)


def a(x):
    return b(x-1)*2


def b(x):
    return x-4


def c(x, y):
    if x % 2 == 0:
        return x + 3 * y
    else:
        return x-y


print(c(5, b(8)))
print(c(a(3), b(5)))

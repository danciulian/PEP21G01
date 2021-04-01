# """ Homework 3 - needs to be presented before exam day"""
#
#
# # 25P
# # Write a function that takes in a list of objects and converts each object in the list into a int.
#` # For objects that can't be directly converted to int should have their length counted
# # The function will return a list with a int values ordered from largest to smallest.
# # example [1, True, '123', False, 6, ()] will be transformed into [123, 6, 1, 1, 0, 0]
#
def ordered_ints(list_of_objects):
    my_list = list_of_objects
    new_list = []
    for i in my_list:
        try:
            new_list.append(int(i))
        except Exception:
            if type(i) == int:
                new_list.append(i)
            elif (type(i) == str) or (type(i) == dict) or (type(i) == list) or (type(i) == tuple):
                l = len(i)
                new_list.append(l)
            elif type(i) == float:
                k = str(i)
                l = len(k)
                new_list.append(l)
            elif i == None:
                new_list.append(0)
    unordered_list = new_list
    l_unordered_list = len(unordered_list)
    for i in range(l_unordered_list):
        for j in range(l_unordered_list-1):
            if unordered_list[j] < unordered_list[j+1]:
                unordered_list[j], unordered_list[j+1] = unordered_list[j+1], unordered_list[j]
    return unordered_list
print(ordered_ints([1, True, '123', None, False, 6, (), (1,2,3,4,5,6,7,8,9,10), {"ana":"are", "mere":"pere","ana":"are", "mere":"pere","ana":"are", "mere":"pere"}]))
print(ordered_ints([1, True, '123', False, 6, ()]))
#
#
# # 25P - (do not rush to resolve this)
# # For recursive functions try reading the articles below if you find need more information
# # https://realpython.com/python-thinking-recursively/
# # https://www.python-course.eu/python3_recursive_functions.php
# # After reading the above articles try creating a function to calculate the series (1^2)+(2^2)+(3^2)...(n^2)
# # The function will receive an int that indicate the number of iterations, or how many times we have (x^2)+
# # when resolving try using this logic: 1^2+2^2 is 1^2+(1^2+1^2)^2
#
###METODA1####
def sum_of_square(n):
    suma = 0
    for i in range(1, n + 1):
        suma = suma + (i ** 2)
    return suma
print(sum_of_square(2))

###METODA2####
def sum_of_square(n):
    if n <= 1:
        return 1
    else:
        return (n ** 2) + sum_of_square(n - 1)
print(sum_of_square(3))


#
# # 25P
# # Write a function that will calculate factorial of numbers squared.
# # For n = 3 the function should calculate (1^2)*(2^2)*(3^2)
#
###METODA1####
def factorial_of_squares(n):
    if n <= 1:
        return 1
    else:
        product = 1
        for i in range(1, n + 1):
            product = product * (i ** 2)
    return product


print(factorial_of_squares(3))


###METODA2####
def factorial_of_squares(n):
    if n <= 1:
        return 1
    else:
        return (n ** 2) * factorial_of_squares(n - 1)


print(factorial_of_squares(5))
#
#
# # 25P
# # Write a function that takes in a string as argument and returns a tuple after performing the following actions:
# # - the string is split after the first encountered space.
# # - all letters in the first half will be transformed to upper case letters
# # - all characters that are not lower-case letters in the second half will be replaced with "_"
# # - returned tuple contains the two processed strings
# # example: "1234567a Text to te5t" will become ("1234567A", "_ext_to_te_t")
#
def process_text(text):
    new_text = tuple(text.split(" ", 1))
    tuple01 = new_text[0]
    tuple02 = new_text[1]

    l01 = len(tuple01)
    result01 = ""
    for i in range(0, l01):
        x = ord(tuple01[i])
        if x >= 97 and x <= 122:
            result01 = result01 + chr(x - 32)
        else:
            result01 = result01 + chr(x)

    l02 = len(tuple02)
    result02 = ""
    for i in range(0, l02):
        y = ord(tuple02[i])
        if y < 97 or y > 122:
            result02 = result02 + chr(y).replace(chr(y), "_")
        else:
            result02 = result02 + chr(y)
    return (result01, result02)


print(process_text('1234567a Text to te5t'))

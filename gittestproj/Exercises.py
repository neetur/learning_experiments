
#2. Write a Python program to get the Python version you are using.
def exercise2() :
    import sys
    print(sys.version)
    return

import datetime
#3. Write a Python program to display the current date and time.
def exercise3 () :
    now = datetime.datetime.now()
    print("Today: "+now.today +'\n')
    print("Time: "+ now.time)
    return

import io
#4. Write a Python program which accepts the radius of a circle from the user and compute the area.
def exercise4() :
    radius = input("Enter the radius: ")
    try:
        r = float(radius)
    except:
        print("Need and Integer")
    area = 3.14 * radius * radius
    print("Area: " + str(area))
    return

#5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them
def exercise5() :
    name = str (input("Enter your first and last name: "))
    x = name.split()
    try:
        print(x[-1] + " " + x[-2])
    except: 
        print("some error")

# Learn Python for Data Science: Chapter 2: Convert from farenheit to celcius and back
def convert_to_Celcius():
    value = int(input("Please enter farenheit number to convert: "))
    RATIO = 5/9
    CONST = 32
    return (value - CONST) * RATIO


# 2. Write a Python program to count the number of characters (character frequency) in a string. 
# https://www.w3resource.com/python-exercises/string/
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

def return_f2l2(str1): 
    if len(str1) < 2:
        return ''

    return(str1[:2]+str1[-2:])

def add_suffix(inputstr):
    if "ing" == inputstr[-3:]:
        return (inputstr+"ly")
    else:
        return (inputstr+"ing")


if __name__ == "__main__":
     print(add_suffix("abc"))
     
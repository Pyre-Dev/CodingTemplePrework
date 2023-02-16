#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

def hello_name(user_name):
    print("hello_"+user_name.upper())

hello_name("USERNAME")

#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for x in range(1, 101):
        if x % 2 !=0:
            print(x, end=" ")

first_odds()

#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list

def max_num_in_list(a_list):
    a_list.sort
    print("The largest number is:", a_list[-1])

max_num_in_list([1,6,5,2,88])

#Question 4
#Write a function to return if the given year is a leap year.

def is_leap_year(a_year):
    if((a_year % 400 == 0) or
       (a_year % 100 != 0) and 
        (a_year %4 == 0)):
        print("YES This is a leap Year")
    else:
        print("NO This is not a leap year")
    
is_leap_year(1999)
is_leap_year(1996)

#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers.

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

print(is_consecutive([1,2,3,4,5,6]))
print(is_consecutive([1,2,3,4,5,67]))


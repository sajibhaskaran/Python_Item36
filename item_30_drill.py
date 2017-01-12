# Item 36

# Assigning variables
print('*********************************')
num_one = 15
str_one = "Check out the String"
fl_one = 35.15



# Printing out the values
print('Integer: {}, String: {},  Float: {}'.format(num_one, str_one, fl_one))

print('*********************************')

# Math operators
add_numbers = num_one + fl_one
sub_numbers = fl_one - num_one
mult_numbers = add_numbers * sub_numbers
div_numbers = add_numbers / sub_numbers
div_numbers += mult_numbers
mod_result = mult_numbers % div_numbers


# Logical Operators: and, or, not

first_num = 20
second_num = 30

if(first_num and second_num):
    print('({} and {}) is true'.format(first_num, second_num))

if(first_num or second_num):
    print('({} and {}) is true'.format(first_num, second_num))
    
if(not(first_num == second_num)):
   print('({} is equal to {}) is false'.format(first_num, second_num))

print('*********************************')
# Conditional operators: if, elif, else

if(first_num > second_num):
    print('{} is bigger than {}'.format(first_num, second_num))
elif(first_num < second_num):
    print('{} is smaller than {}'.format(first_num, second_num))
else:
    print('{} is equal to {}'.format(first_num, second_num))

print('*********************************')

# While loop
    
number = 1
while number <= 10:
    print('{} X 5 = {}'.format(number, number*5))
    number += 1
    
print('*********************************')

# For loop

for number in range(1,11):
     print('{} X 5 = {}'.format(number, number*5))

print('*********************************')

# Iterating through a list


my_list = ['one', 'two', 'three', 'four', 'five']

for item in my_list:
    print(item)

print('*********************************')

# Iterating through a tuple

my_tuple = ("HTML", "CSS", "JavaScript", 2016, 2017)

for item in my_tuple:
    print(item)

print('*********************************')

# Defining a function

def my_func():
    return "Tech Academy"

# Calling that function

print(my_func())





                
                
          

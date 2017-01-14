'''
DRILL:

Write your own version of the sorted() method in Python. This method should take a list as an argument
and return a list that is sorted in ascending order. Call your method passing in the following lists as
arguments and print out each sorted list to the shell. This should be an algorithm that you write.
Do not use .sort() or the sorted() methods in your method.

[67, 45, 2, 13, 1, 998]

[89, 23, 33, 45, 10, 12, 45, 45, 45]

'''



def sorted(x):
    for len_list in range(len(x)-1, 0, -1):
        for i in range(len_list):
            if x[i] > x[i+1]:
                x[i],x[i+1] = x[i+1],x[i]
                





list1=[67, 45, 2, 13, 1, 998]

sorted(list1)
print(list1)

list2=[89, 23, 33, 45, 10, 12, 45, 45, 45]

sorted(list2)
print(list2)

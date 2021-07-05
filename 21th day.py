"""1.	Write a program using zip() function and list() function,
create a merged list of tuples from the two lists given."""
l1 = [2, 4, 6, 8]
l2 = ['a', 'b', 'c', 'd']
l3 = list(zip(l1, l2))
print("Merged List Of Tuples : ", l3)

"""2.	First create a range from 1 to 8. Then using zip, m
erge the given list and the range together to 
create a new list of tuples"""
list1 = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx']
l4 = list(range(1,8))
l5 = zip(list1,l4)
print(l5)


# 3.Using sorted() function, sort the list in ascending order.
B = [67788,8990,8043,2,579,78,88888]
C = sorted(B)
print("List In Ascending Order : ", C)

"""4.	Write a program using filter function, filter
the even numbers so that only odd numbers are passed to the new list.
"""
P = [ 13, 30, 29, 67, 89, 100, 50, 60]
Q = list(filter(lambda x : x % 2 == 1, P))
print("Odd Number in New List ", Q)
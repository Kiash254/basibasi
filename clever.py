from ntpath import join
import turtle

from numpy import append
from xcffib import Union
#making a square
# qazi_turtle=turtle.Turtle()
# qazi_turtle.forward(100)
# qazi_turtle.right(90)
# qazi_turtle.forward(100)
# qazi_turtle.right(90)
# qazi_turtle.forward(100)
# qazi_turtle.right(90)
# qazi_turtle.forward(100)
# qazi_turtle.right(90)
#function
# def sqaure():
#     qazi_turtle=turtle.Turtle()
#     qazi_turtle.forward(100)
#     qazi_turtle.right(90)
#     qazi_turtle.forward(100)
#     qazi_turtle.right(90)
#     qazi_turtle.forward(100)
#     qazi_turtle.right(90)
#     qazi_turtle.forward(100)
#     qazi_turtle.right(90)
   
# sqaure()
# turtle.forward(500)
#if else statement
# elephant=3000
# ant=0.5

# if (elephant>ant):
#     sqaure()
# else:
#     turtle.forward(100)


#a simple if else statement

#while loops

# qazi='happy'
# while qazi=='sad':
#     qazi_turtle.forward(20)

 
# for count in range(4):
#     sqaure()
    










# import calendar

# print(calendar.weekheader(9))

# print()
# print(calendar.firstweekday())
# print()

# print(calendar.month(2022,3))


# print(calendar,calendar.monthcalendar(2022,3))
# print()

# print(calendar.calendar(2022))



# days_week=calendar.weekday(2022,3,25)
# print(days_week)

# is_leap=calendar.isleap(2022)
# print(is_leap)


# how_many_leap=calendar.leapdays(2020,2022)
# print(how_many_leap)

# import datetime
# import time


#type casting data conversion
x=2.9
y=int(x)
print(y)

#strings in python
#block of statements in quotation marks

v="hello mum  i miss you"
print(len(v))
print(v)

#List in python

v=["kiash",'Noms','God','with','Us']

for Noms in(v):
    print('God please lead us not to temptation')


l1=[1,2,3,4,5]
l2=['hallo','we','hava','meeting','kindly avail']
l3=l1+l2
print(l3)
#append,delete.reverse,indexing
name=['joe','john','james']
print('before append',name)
name.append('kiash')
print('after append',name)

#insert adds objects anywhere in the list
name.insert(0 ,'Noms')
print(name)
#remove
name.remove('kiash')
print(name)
#sorting
print(name.sort())



#reverse
name.reverse()
print(name)
#sorting numbers
l4=[1,2,3,4,8,5,99,10]
print(l4)
l4.sort()
print(l4)

#itarate over the list using for lpooop
for num in l4:
    print("we are programmers")


#indexing and slicing a list

#indexing
n=[0,4,5,5,6,8]
print(n[-5])

#slicing

print(n[:3])
print(n[3:])
name='first last'
print(name[5:])
print(name[:5])

#striking
print(n[::2])
winsize=3
less=2
for i in range(len(n)-less):
    print(n[0:])
#dyanamic slicing
for i in range(len(n)):
    print(n[i:i+winsize])


#join and spilt in functions

import csv
#split


    # never='bad','good','emtions','lovely'

    # print(never)
    # #deleimter
    # l=never.split("good")
    # print(l)
#join

#tuples-list with parentehes

t=('name','kiash','nomes')
print(t)


credit=(585684397737347845,'kiash','owner','credited to','my love Naomi')
credit2=(758458784578458785,'Gift','Giftd me maaan','A credit was owesome',9334)

credits=(credit ,credit2)
print(credits)
#sets holds list of data using Curly braces

#unorded,no duplication,casting a list
sets={'mango','banana','grapes'}
#no duplication of values 
#how to automate stuffs with python
num={1,2,3,3,4,5,6,6,6}

sets.add('jinja')
sets.add(9)
print(sets)
sets.add('onions')
print(sets)
print(num)

lib={'karatina','peter','lorem','Dkut'}
lib2={'loren','lorem','duvet'}
#ven diagram
v=lib.intersection(lib2)
l=lib.union(lib2)
print(v)
print(l)

div=lib.difference(lib2)
print(div)

#dictionaries stores data iin keys and values


dict1={'name':'kiash','age':23,'courese':'computer scince'}
dict2={'hobbies':'playsation','career':'football'}
#elements  are accesd using keys 

print(dict1['name'])
print(dict2['career'])
























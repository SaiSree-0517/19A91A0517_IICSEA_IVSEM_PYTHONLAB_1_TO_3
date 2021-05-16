#1.1) Running instructions in Interactive interpreter and a Python Script
#Interactive interpreter
>>> a=10
>>> print(a)
10
>>> type(a)
<class 'int'>
>>> a=15
>>> b=24
>>> c=a+b
>>> print(c)
39
>>> s='hello'
>>> type(s)
<class 'str'>
>>> len(s)
5
>>> 
#python script to get the bill amount
pa=int(input('enter the bill amount:'))
if pa>=1000:
    d=0.1*pa
    print('discount=',d)
else:
    d=0.05*pa
    print('discount=',d)
a=pa-d
print(a)
#output
enter the bill amount:1500
discount= 150.0
1350.0

#1.2) Implement a python script to purposefully raise Indentation Error and Correct it
#with indentation error
i=1
while i<=10:
print(i)#indentation error
    i+=1
print('i=',i)
#after correcting indentation error
i=1
while i<=10:
    print(i)
    i+=1
print('i=',i)
#output:
1
2
3
4
5
6
7
8
9
10
i= 11
>>> 

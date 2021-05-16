"""
2.2Implement a python script add.py that takes 2
numbers as command line arguments and perform arithmetic operations on them.

"""
import sys
n1=int(sys.argv[1])
n2=int(sys.argv[2])
print('Sum=',(n1+n2))
print('Sub=',(n1-n2))
print('Div=',(n1/n2))
print('Floordiv=',(n1//n2))
print('Mul=',(n1*n2))
print('exp=',(n2**2))
print('Mod=',(n1%n2))
#output
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

C:\Users\Satyanarayana G\Desktop\python programs>add.py 10 2
Sum= 12
Sub= 8
Div= 5.0
Floordiv= 5
Mul= 20
exp= 4
Mod= 0

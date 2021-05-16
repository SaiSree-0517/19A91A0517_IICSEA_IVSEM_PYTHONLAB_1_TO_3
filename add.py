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

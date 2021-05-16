"""
2.1Implement a python script to compute
distance between two points taking inp from the user (Pythagorean Theorem)
"""
x1=int(input("enter x1 : "))

x2=int(input("enter x2 : "))

y1=int(input("enter y1 : "))

y2=int(input("enter y2 : "))

result= ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)

print("distance between",(x1,y1),"and",(x2,y2),"is : ",result)
#output
enter x1 : 5
enter x2 : 6
enter y1 : 7
enter y2 : 8
distance between (5, 7) and (6, 8) is :  1.4142135623730951

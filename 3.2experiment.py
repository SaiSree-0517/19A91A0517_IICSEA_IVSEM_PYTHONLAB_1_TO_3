"""
3.2) Implement a python script using
for loop that loops over a sequence
"""
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))  
for num in range(start, end + 1):
     # checking condition
        if num % 2 == 0:
            print(num, end = " ")          
#output
Enter the start of range: 2
Enter the end of range: 12
2 4 6 8 10 12

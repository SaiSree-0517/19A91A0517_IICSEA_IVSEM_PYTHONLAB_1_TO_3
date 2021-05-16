n=int(input('enter the number'))
rev=''
while n:
    r=n%10
    rev=rev+str(r)
    n=n//10
rev=rev[::-1]
for i in range(0,len(rev)):
    if rev[i]=='1':
        print('one',end=" ")
    elif rev[i]=='2':
        print('two',end=" ")
    elif rev[i]=='3':
        print('three',end=" ")
    elif rev[i]=='4':
        print('four',end=" ")
    elif rev[i]=='5':
        print('five',end=" ")
    elif rev[i]=='6':
        print('six',end=" ")
    elif rev[i]=='7':
        print('seven',end=" ")
    elif rev[i]=='8':
        print('eight',end=" ")
    elif rev[i]=='9':
        print('nine',end=" ")
    else:
        print('zero',end=" ")
#output
enter the number 4000
four zero zero zero 

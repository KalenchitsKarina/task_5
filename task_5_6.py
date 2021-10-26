from random import randint

while True:
    n=input('Enter size of array : ')
    if n.isdigit()==True:
        n=int(n)
        break
    else:
        print('n is not digit, try again!')
        continue
a=[randint(0,50) for i in range(n)]
print(a)

f=0
for i in range(n-1):
    if a[i]>a[i+1]:
        f+=1
print (f)
ls={}
sum=0
for i in range (200,301):
    for j in range (2,i):
        if i%j==0:
            sum+=j
    ls[i]=sum
print (ls)

for i in range (200,300):
    zn=ls[i]
    for j in range (i+1,300):
        if zn==ls[j]:
            print(j,':',ls[j],'   ',i,':',ls[i])

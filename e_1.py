#Создать квадратную матрицу размерностью n и 
#заполнить ее случайными значениями от 1 до 9.
 
'''
from random import randint 
n=int(input('Enter the size of the matrix : '))
ls=list()
for i in range (0,n):
   ls.append ([])

for i in ls:
    for j in range (n):
        i.append(randint(1,9))
print (ls)
'''
# то же самое с помощью генераторов 
'''
import random
n=3
matrix =[]
tm =[ [random.randint (1,9) for y in range (n)] for x in range (n)]
print (tm)
'''
#Создать квадратную матрицу размерностью n и 
#заполнить ее случайными значениями. 
#Найти сумму всех элементов матрицы,которые кратны 3.
'''
import random

n=int(input('Enter the size of matrix : '))
#matrix[] оно вроде и не надо
tm=[[random.randint(1,9) for y in range(n)] for y in range(n)]
print (tm)

sum=0
for i in range (n):
    for j in range (n):
        if tm[i][j]%3==0:
            sum+=tm[i][j]
print ('Sum of all elements that are multiples of 3 is',sum)
'''
#Дан двумерный массив n × m элементов. Определить,
#сколько раз встречается число 7 среди элементов массива.[02-4.2-BL12]

'''
from random import randint

n=int(input('Enter n: '))
m=int(input('Enter m: '))

f=0
ls=[]
for i in range(n):
    ls.append([])

for i in ls:
    for j in range(m):
        i.append(randint(1,9))

for i in range(n):
    for j in range(m):
        if ls[i][j]==7:
            f+=1

print (ls)
print ('In array',f,'elements "7"')
'''

#Дана целочисленная матрица А[n,m]. Посчитать 
#количество элементов матрицы, превосходящих 
#среднее арифметическое значение элементов 
#матрицы и сумма индексов которых четна.[02-4.2-BL23]

'''
import random
n=2
m=3
mat=[[random.randint(0,20)for i in range(m)]for i in range(n)]
sum=0
print (mat)
for i in range(n):
    for j in range(m):
        sum+=mat[i][j]
print(sum) #всех элементов матрицы
f=0
average=sum/(n*m)
print (average)
for i in mat:
    for j in i:
        if j>average:
            f+=1
print (f) # количество элементов больше ср.арифм.
e=0
for n,m in enumerate (mat):
    for i,a in enumerate (m):
        if a>average and (n+i)%2==0:
            e+=1
print (e)
'''

#Создать список учеников подобной структуры.
#Определить средний балл оценок по всем предметам, 
#и вывести сведения о студентах, средний балл которых больше 4. [02-7.3-BL-02]

average = 0
urok = 0
pupls=[
{
    'firstname' : 'Masha',
    'group': 42,
    'physics': 8,
    'informatics' : 9,
    'history' : 8
},
{
    'firstname' : 'Masha1',
    'group': 42,
    'physics': 8,
    'informatics' : 8,
    'history' : 10
},
{
    'firstname' : 'Masha2',
    'group': 42,
    'physics': 4,
    'informatics' : 6,
    'history' : 8
}
]
for i in pupls:
    average=0
    urok=0
    for a,r in i.items():
        if a=="firstname" or a=='group':
            continue
        
        #average+=pupls[a]
        urok+=1
    x=average/urok 
    if x>=4:
        print (i)



#Написать игру. Пользователь должен угадать число.
#Сперва вводиться диапазон угадывания. После 
#колличество попыток. В случае правильного ответа -
#выводить You are the winner. В случае неправильного 
#давать игроку подсказку(больше или меньше искомое число).
#Если за указанное количество попыток число не угадано - 
#выводить: You are the loser и правильное число.
 
'''
from random import randint
n=int(input('Enter the lower limit of the range : '))
m=int(input('Enter the upper limit of the range : '))
kolvo=int(input('Enter the number of attempts : '))

chislo= randint(n,m)

for i in range (kolvo):
    r = int(input('Your turn, please : '))
    if r !=chislo:
        if r>chislo:
            print('Need less !')
        else:
            print ('Need more !')
    else:
        print ('You are the winner')
        break
else:
    print ('You are the loser')
    print (f'chislo = {chislo} ')
'''


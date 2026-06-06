expensis=[["January",2200],["Februry",2350],['March',200],['April',2130],["May",2190]]

print(f'We spent extra {expensis[1][1]-expensis[0][1]}$ in Febrary.')

print(f'We spent {expensis[0][1]+expensis[1][1]+expensis[2][1]}$ in First three months.')

for i in range(0,len(expensis)):
    if expensis[i][1]==2000:
        print(f'In month {expensis[i][0]} we spent exectly 2000$.')
    
expensis.append(['June',1910]) 

expensis[3][1]=expensis[3][1]-2000

for i in range(0,len(expensis)):
    print(f'{expensis[i][0]}  {expensis[i][1]}')

#-------------------------------------#

heros=['Spider Man','Thor','Hulk','Caption America']

print(len(heros))

heros.append('Black Panther')
print(heros)

heros.remove('Black Panther')
heros.insert(3,'Black Panther')
print(heros)

heros.insert(2,'Doctor Jery')
del heros[3:5]
print(heros)

heros.sort()
print(heros)

#-------------------------------------#
maxnumber=int(input('Enter a number: '))
odd=[i for i in range(1,maxnumber,2)]

print(odd)
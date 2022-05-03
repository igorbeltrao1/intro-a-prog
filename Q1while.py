
#usando o "while"
num = [0, 6, 8, 9, 4, 8, 9, 23, 14, 78, 2, 3, 6, 45, 13, 13, 13, 45, 96, 74]

print(f'a lista é essa : {num}')

lista = len(num) -1

newnum = []

while lista >= 0:
     newnum.append(num[lista])
     lista = lista -1
 
print(f'a lista invertida fica assim: {newnum}')  
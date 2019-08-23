##
## Imprima la suma de la segunda columna.
##

abrir=open('data.csv','r').readlines()
colum=[int(row[2]) for row in abrir]
x=(sum(colum))
print(x)

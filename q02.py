##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##

abrir=open('data.csv','r').readlines()
c=([row[0] for row in abrir])
for i in sorted(set(c)): 
  c1=c.count(i)
  print(f"{i},{c1}")

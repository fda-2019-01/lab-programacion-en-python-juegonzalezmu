##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##

data=open('data.csv','r').readlines()
data=[row.split('\t') for row in data]
x=dict()
for row in data: 
  if row[0] not in x.keys():
    x[row[0]]=0
  x[row[0]]=x[row[0]]+int(row[1])
for i in sorted(x.keys()):
  print(i,',',x[i],sep='')

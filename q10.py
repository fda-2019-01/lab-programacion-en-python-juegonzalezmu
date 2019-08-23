##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
data = open('data.csv','r').readlines()
data = [line[:-1] for line in data]
data = [line.split('\t') for line in data]
a=[row[4].split(',') for row in data]
b=','.join([row[4] for row in data]).split(',')
b=[row.replace('\n','').split(':') for row in b]
df=([row[0] for row in b])
for i in sorted(set(df)):
  print(f'{i},{df.count(i)}')

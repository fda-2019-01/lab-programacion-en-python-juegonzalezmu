##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##

d = open('data.csv','r').readlines()
d = [line[:-1] for line in d]
d = [line.split('\t') for line in d]
X = [line[2].split('-')[1] for line in d]
a = set(X)
for i in sorted(a):
    print(i+','+str(X.count(i)))

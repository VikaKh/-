import time
import random  
#нахождение минимального элемента, исключая текущий элемент
def Min(lst,myindex):
    return min(x for idx, x in enumerate(lst) if idx != myindex)

#удаление нужной строки и столбца
def Delete(matrix,index1,index2):
    del matrix[index1]
    for i in matrix:
        del i[index2]
    return matrix


matrix=[]
H=0
n=10
PLenght=0
ind1=[]
ind2=[]
res=[]
result=[]
FirstMatrix=[]


for i in range(n):
    ind1.append(i)
    ind2.append(i)

start_time = time.time()
#создаем матрицу
def creatMatrix():
    r = 0
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(random.randint(0,100))
            r += 1  
 
    return matrix
 
print(creatMatrix())


for i in range(n):FirstMatrix.append(matrix[i].copy())

#Присваеваем главной диагонали float(inf)
for i in range(n): matrix[i][i]=float('inf')

while True:
    #Вычитаем минимальный элемент в строках
    for i in range(len(matrix)):
        temp=min(matrix[i])
        H+=temp
        for j in range(len(matrix)):
            matrix[i][j]-=temp

    #Вычитаем минимальный элемент в столбцах    
    for i in range(len(matrix)):
        temp = min(row[i] for row in matrix)
        H+=temp
        for j in range(len(matrix)):
            matrix[j][i]-=temp
  
    #Оцениваем нулевые клетки и ищем нулевую клетку с максимальной оценкой
    NullMax=0
    index1=0
    index2=0
    tmp=0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]==0:
                tmp=Min(matrix[i],j)+Min((row[j] for row in matrix),i)
                if tmp>=NullMax:
                    NullMax=tmp
                    index1=i
                    index2=j
    
    res.append(ind1[index1]+1)
    res.append(ind2[index2]+1)	
    oldIndex1=ind1[index1]
    oldIndex2=ind2[index2]
    if oldIndex2 in ind1 and oldIndex1 in ind2:
        NewIndex1=ind1.index(oldIndex2)
        NewIndex2=ind2.index(oldIndex1)
        matrix[NewIndex1][NewIndex2]=float('inf')
    del ind1[index1]
    del ind2[index2]
    matrix=Delete(matrix,index1,index2)
    if len(matrix)==1:break	

for i in range(0,len(res)-1,2):
	if res.count(res[i])<2:
		result.append(res[i])
		result.append(res[i+1])
for i in range(0,len(res)-1,2):
	for j in range(0,len(res)-1,2):
		if result[len(result)-1]==res[j]:
			result.append(res[j])
			result.append(res[j+1])
print("----------------------------------")
print(result)

#Считаем длину пути
for i in range(0,len(result)-1,2):
    if i==len(result)-2:
        PLenght+=FirstMatrix[result[i]-1][result[i+1]-1]
        PLenght+=FirstMatrix[result[i+1]-1][result[0]-1]
    else: PLenght+=FirstMatrix[result[i]-1][result[i+1]-1]
print(PLenght)
print("--- %s seconds ---" % (time.time() - start_time))
print("----------------------------------")
input()
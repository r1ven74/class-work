import random
num_1 = int(input("введите число"))
num_2 = int(input("введите число"))
matrix = [[random.randint(1,10)for i in range(num_1)] for j in range(num_2)]

for row in matrix:
    for element in row:
        print(element, end='\t')#Ставит в конце таб
    print()#перенос строки
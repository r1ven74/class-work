numbers = list(map(int, input("введите сторону квадрата").split())) # нахождение площади квадрата
print(numbers[0]**2)

numbers = list(map(int, input("введите стороны прямоугольника через пробел").split())) #нахождение периметра прямоугольника
print(numbers[0]*2+numbers[1]*2)

numbers = list(map(int, input("введите радиус круга").split())) #нахождения площади круга
print(numbers[0]*2 *3.14)

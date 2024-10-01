numbers = list(map(int, input("введите сторону квадрата").split()))
print(numbers[0]**2)

numbers = list(map(int, input("введите стороны прямоугольника через пробел").split()))
print(numbers[0]*2+numbers[1]*2)

numbers = list(map(int, input("введите радиус круга").split()))
print(numbers[0]*2 *3.14)
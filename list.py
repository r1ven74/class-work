lst = [67, 40, 344, 143, 875, 9, 123, 672, 216, 975, 1043, 494, 333, 9834, 2, 5, 6, 4]
lst.append(232323232)
print(lst)

lst_2 = [3,6,457,765,24,53,6,31,48,5798,42,8,67,4,96,95,235]
lst.extend(lst_2)
print(lst)

lst.insert(6, 66)
print(lst)

lst.remove(66)
print(lst)

lst.pop(6)
print(lst)

print(lst.index(6))

print(lst.count(9))


lst.sort()
print(lst)


lst.reverse()
print(lst)

lst.copy()
print(lst)

lst.clear()
print(lst)
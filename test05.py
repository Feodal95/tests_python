#Посчитать количество символов в верхнем регистре
a = input()
print(sum(1 for x in a if x.isupper()))
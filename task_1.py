B = list(map(int, input("Введіть елементи списку через пробіл: ").split()))

s = 0

if 0 in B:
    Zero_index = B.index(0)
    for i in range(Zero_index+1, len(B)):
       s+=abs(B[i])
else:
    s = 0

print("Сума модулів після першого нуля:", s)

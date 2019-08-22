import math

x = input("introduce el número de elementos: ")
y = input("introduce el número de combinaciones posibles: ")

num= int(x)
num2= int(y)
elementos = math.factorial(num)
combinaciones=math.factorial(num2)

resultado = elementos / (elementos-combinaciones)*combinaciones


print("Las combinaciones posibles son: ",resultado)

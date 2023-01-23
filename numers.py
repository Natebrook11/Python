#todosa los numeros impares hasta el seleccionado
while(True):
 num = int(input("Ingrese un numero entero: "))
 print('Estos son los numeros impares:')
 for x in range(1, num+1, 2): 
 	print(x, end=", ")
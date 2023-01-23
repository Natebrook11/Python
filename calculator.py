#First input
num1 = float(input("First num:"))
#Secont input
num2 = float(input("Secont digit:"))
#Operation digit
print("Simbols:: Add (+) Rest (-) Multipli (*) Division (/)")
op = input("Enter the opertaion:")

if op == "+": #Suma
    result = num1 + num2 
    print(result)
if op == "-": #Resta
    result = num1 - num2 
    print(result)
if op == "*": #Multiplicacion
    result = num1 * num2 
    print(result)
if op == "/": #Division
    result = num1 / num2 
    print(result)
else :
    print("Error invalid operation simbol")


import time

'''
for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print("BOOOOOMMMMMM!!!")
'''

while True:
    minuto = int(input("Introduce los minutos: "))
    segundo = int(input("Introduce los segundos: "))
    
    total_segundos = minuto *60 + segundo
    
    while total_segundos > 0:
        print(total_segundos)
        total_segundos -=1
        time.sleep(1)
    print("BOOOOOMMMMMM!!!")
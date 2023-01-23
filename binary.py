from colorama import *
init()
def toBinary(string):
    binary = ''
    for character in string:
        binary = binary + bin(ord(character))[2:].zfill(8) + ' '
    return binary.strip()
    
banner = """
  ____ _____ _   _          _______     __
 |  _ \_   _| \ | |   /\   |  __ \ \   / /
 | |_) || | |  \| |  /  \  | |__) \ \_/ / 
 |  _ < | | | . ` | / /\ \ |  _  / \   /  
 | |_) || |_| |\  |/ ____ \| | \ \  | |   
 |____/_____|_| \_/_/    \_\_|  \_\ |_|   
                                          
                                         
"""
print(Fore.GREEN+ banner )
print(toBinary(input(Fore.CYAN+'Text : ')))
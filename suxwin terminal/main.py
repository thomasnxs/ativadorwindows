import os
from funcoes import hub, escolha_init

hub()

serial_keys = """
1- Home/Core
2- Home/Core (Country Specific)
3- Home/Core (Single Language)
4- Home/Core N
5- Professional (Windows 10 Pro)
6- Professional N (Windows 10 Pro N)
7- Enterprise
8- Enterprise N
9- Education
10- Education N
11- Enterprise 2015 LTSB
12- Enterprise 2015 LTSB N
13- Enterprise 2016 LTSB
14- Enterprise 2016 LTSB N
"""
escolha_hub = int(input(": "))

if escolha_hub == 1: 
    os.system("cls")
    print("Selecione o Modelo de seu Windows")
    print(serial_keys)
    escolha_init()
elif escolha_hub == 2:
    os.system("cls")
    print("Para instalar o Windows, deve executar o programa como adminstrador.")
    print("Escolha o respectivo Windows que você tem instalado e inicie a ativação.")
    print("Durante a instalação apareceram alguns pop-ups, aperte ok em todos e seja feliz.")
    os.system("python main.py")
else:
    os.system("exit")
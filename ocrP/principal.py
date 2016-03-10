# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 08:52:41 2016

@author: Paul
"""
from crearDataset import CreaData
from ClasificacionKNN import knn
from colorama import Fore, Back

objeto1 = CreaData()
objeto2 = knn()
opc = 0
while(opc != 3):
    print(Fore.BLUE+Back.RESET+"\n     Menu")
    opc = int(input("  1.- Crear Dataset\n  2.- Clasificar\n  3.- Salir"+Fore.GREEN+"\n    Opcion: "))
    if(opc == 1):
        objeto1.main()
    elif(opc == 2):
        objeto2.main()
    else:
        print("\n           "+Fore.MAGENTA+"Adios...!")
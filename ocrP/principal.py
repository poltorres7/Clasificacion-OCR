# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 08:52:41 2016

@author: Paul
"""
from crearDataset import CreaData
from ClasificacionKNN import knn

objeto1 = CreaData()
objeto2 = knn()
opc = 0
while(opc != 3):
    print("Menu")
    opc = int(input("1.- Crear Dataset\n2.- Clasificar\n3.- Salir\n  Opcion:"))
    if(opc == 1):
        objeto1.main()
    elif(opc == 2):
        objeto2.main()
    else:
        print("Adios...!")
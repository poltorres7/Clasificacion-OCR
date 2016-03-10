# -*- coding: utf-8 -*-

from PIL import Image
import matplotlib.image as mpimg
import csv
import os
from colorama import Fore
cont = 1

class CreaData():

    op = open('dataset2.csv','a',newline='')
    escribir = csv.writer(op,delimiter=';')
    """
        * Método: Procesar
        * Parametros: Dirección IMG, clase de la imagen
        * Retorna: NoAplica
        * Funcionamiento:
        *  Recibe todas las imagenes que recorre el metodo main, abre las imagenes,
        *  se obtienen las filas y columnas de la IMG, se llama a los diferentes metodos de 
        *  obtención de caracteristicas y los escribe en el archivo dataset2.csv
    """
    def analisis(ruta,clase):
        global cont
        #abrimos imagen
        img = Image.open(ruta)
        img2 = mpimg.imread(ruta)
        col, fil = img.size
        data=[]#arreglo para insertar en el data
        data.extend(CreaData.arraysImg(img2,fil,col))
        data.extend(CreaData.cortes(img2,fil,col))
        data.append(CreaData.razonImagen(col,fil))
        data.append(CreaData.razon_1s_area(col,fil,img2))
        data.append(clase)
        data.append(cont)
        CreaData.escribir.writerow(data)#se escribe en el data
        cont += 1
        
    """
        * Método: razonFC
        * Parametros: Numero de filas y numero de columnas
        * Retorna: la razon de las filas/columnas
        * Funcionamiento:
        *  regresa la division de col/fil
    """
    def razonImagen(col, fil):
        #caracteristica 1 razon
        razon= col/fil
        return razon

    """
        * Método razon_1_img
        * Parametros: Imagen iterable, numero de filas, numero de columnas
        * Retorna: la razon de el numero de 1's/filas*columnas
        * Funcionamiento:
        *  Cuenta el numero de 1's en la imagen y lo divide entre el total de la imagen (filas*columnas)
    """
    def razon_1s_area(columnas,filas,img2):
        #caracteristica 3    1's/tamaño de la imagen(filas*columnas)
        c3_1 = 0
        for x in range(filas):
            for z in range(columnas):
                if(img2[x][z] == 1):
                    c3_1 += 1
        razon = c3_1/(filas*columnas)
        return razon
        
    """
        * Método vectoresImg
        * Parametros: Imagen iterable, numero de filas, numero de columnas
        * Retorna: vector con 6 razones de la imagen, 3 verticales y 3 horizontales
        * Funcionamiento:
        *  Cuenta el numero de 1's en un vector dado de la imagen, 3 verticales y 3 horizontales.
        *  Verticales: mitad de imagen(col/2), cuarto de imagen (col/4) y tres cuartos imagen (3*(col/4))
        *  Horizontales: mitad de imagen(fil/2), cuarto de imagen (fil/4) y tres cuartos imagen (3*(fil/4))
    """
    def arraysImg(img,fil, col):
        vectores = [0,0,0,0,0,0]
        for x in range(fil):
            if(img[x][int(col/2)] == 1):
                vectores[0] += 1
            if(img[x][int(col/4)] == 1):
                vectores[1] += 1
            if(img[x][3*int(col/4)] == 1):
                vectores[2] += 1
    
        for x in range(col):
            if(img[int(fil/2)][x] == 1):
                vectores[3] += 1
            if(img[int(fil/4)][x] == 1):
                vectores[4] += 1
            if(img[3*int(fil/4)][x] == 1):
                vectores[5] += 1
        vec = [0.0,0.0,0.0,0.0,0.0,0.0]
        for i in range(len(vec)):
            if(i<3):
                vec[i] = vectores[i]/fil
            else:
                vec[i] = vectores[i]/col
        return vec
    
    """
        * Método cortes
        * Parametros: Imagen iterable, numero de filas, numero de columnas
        * Retorna: El numero de cortes de la mitad de la imagen y un cuarto de la imagen
        * verticalmente
        * Funcionamiento:
        *  Recorre la imagen en las columnas (col/2) y (col/4), cuenta los cambios de 1's y 0's
        *  y despues divide los cambios entre 2 para determinar los cortes en ese vector.
    """
    def cortes(img2,fil,col):
        corte = [0,0,0,0,0,0]
        mcol = int(col/2)
        col_1_4 = int(col/4)
        col_3_4 = 3*int(col/4)
        
        for x in range(fil):
            if (x == 0 or x == (fil-1)):
                if(img2[x][mcol] == 1):
                    corte[0] += 1
                if(img2[x][col_1_4] == 1):
                    corte[1] += 1
                if(img2[x][col_3_4] == 1):
                    corte[2] += 1
            if(img2[x][mcol] != img2[x-1][mcol] and x != 0):
                corte[0] += 1
            if(img2[x][col_1_4] != img2[x-1][col_1_4] and x != 0):
                corte[1] += 1
            if(img2[x][col_3_4] != img2[x-1][col_3_4] and x != 0):
                corte[2] += 1
        mfil = int(fil/2)
        fil_1_4 = int(fil/4)
        fil_3_4 = 3*int(fil/4)
        
        for x in range(col):
            if (x == 0 or x == (col-1)):
                if(img2[mfil][x] == 1):
                    corte[3] += 1
                if(img2[fil_1_4][x] == 1):
                    corte[4] += 1
                if(img2[fil_3_4][x] == 1):
                    corte[5] += 1
            if(img2[mfil][x] != img2[mfil][x-1] and x != 0):
                corte[3] += 1
            if(img2[fil_1_4][x] != img2[fil_1_4][x-1] and x != 0):
                corte[4] += 1
            if(img2[fil_3_4][x] != img2[fil_3_4][x-1] and x != 0):
                corte[5] += 1
        return corte
    
    def main(self):
        cont = 0
        for base, dirs, files in os.walk('C:/Users/Paul/Desktop/OCR/ocrP/data'):       
            #print(base)
            if cont > 0:
                print(Fore.BLUE+"    Obteniendo caracteristicas de: "+ Fore.BLACK+ str(base[len(base)-1]))
                for name in files:
                    CreaData.analisis((str(base)+'/'+name),base[len(base)-1])
            cont += 1
        CreaData.op.close()#se cierra la escritura
        print(Fore.MAGENTA+"     Proceso finalizado!")
    def __init__(self):
        pass
    
import csv
import math
import operator
from PIL import Image
import matplotlib.image as mpimg
from crearDataset import CreaData

trainingSet = []

class knn():

    def cargarDataset(archivo):
        global trainingSet
        with open(archivo, newline='') as csvfile:
            lines = csv.reader(csvfile, delimiter= ';')
            dataset = list(lines)
            for x in range(len(dataset)-1):
                for y in range(13):
                    #print(dataset[x][y])
                    dataset[x][y] = float(dataset[x][y])
                trainingSet.append(dataset[x])
        csvfile.close()

    def euclideanDistance(instance1, instance2, length):
        distance = 0
        for x in range(length):
            distance += pow((instance1[x] - instance2[x]), 2)
        return math.sqrt(distance)

    def getNeighbors(testInstance, k):
        global trainingSet
        distances = []
        length = len(testInstance)-1
        for x in range(len(trainingSet)):
            dist = knn.euclideanDistance(testInstance, trainingSet[x], length)
            distances.append((trainingSet[x], dist))
        distances.sort(key=operator.itemgetter(1))#ordena de menor a mayor
        neighbors = []
        for x in range(k):
            #print(distances[x])
            print("Linea(Instancia): "+str(distances[x][0][15])+ " Clase: "+str(distances[x][0][14])+" Distancia: "+str(distances[x][1]))
            neighbors.append(distances[x][0])
        return neighbors

    def getResponse(neighbors):
        classVotes = {}
        #print(neighbors)
        for x in range(len(neighbors)):
            response = neighbors[x][-2]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0]

    def obtenerCaract(self,ruta):
        data = []#se declara arreglo para guardar las caaracteristicas
        img = Image.open(ruta) #Abre imagne
        img2 = mpimg.imread(ruta) #Abre imagen
        columnas, filas = img.size #Se obtienen las filas y columnas

        #Se insertan datos en el array data
        data.extend(CreaData.arraysImg(img2,filas,columnas))
        data.extend(CreaData.cortes(img2,filas,columnas))
        #print(CreaData.cortes(img2,filas,columnas))
        data.append(CreaData.razonImagen(columnas,filas))
        data.append(CreaData.razon_1s_area(columnas,filas,img2))
        return data

    def __init__(self):
        pass

    def main(self):
        global trainingSet
        data =[]
        knn.cargarDataset('dataset2.csv')
        input("Se finalizo la carga de dataset, presione ENTER para continuar... : ")
        #print(knn.trainingSet)
        ruta = 'C:/Users/Paul/Desktop/OCR/ocrP/test/'
        ruta += input("Ingresa el nombre de la imagen: ")
        data = knn.obtenerCaract(self,ruta)
        k = int(input("Ingresa el numero K: "))
        resultado = knn.getResponse(knn.getNeighbors(data,k))
        print("\n   La imagen es un: "+str(resultado))
#        print(len(trainingSet))
        del trainingSet[:]
#        print(len(trainingSet))
        
        
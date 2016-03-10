import csv#libreria para escribir dataset
import math#libreria para  sacar la raiz
import operator#libreia para ordenar dataset
from PIL import Image#libreria para abrir imagen
import matplotlib.image as mpimg#libreria para abrir imagen iterable
from crearDataset import CreaData#clase para crear dataset
from colorama import Fore, Back#clase para tener colores en texto

trainingSet = []#arreglo que contendra el dataset

class knn():#se declara clase
    """
        * Método cargarDataset
        * Parametros: nombre del archivo a abrir
        * Retorna: N-A
        * Funcionamiento:
        *  Lee el archivo y guarda los datos como float, cuenta el numero de clases en el dataset
        *  y muestra información general del dataset
    """
    def cargarDataset(archivo):
        global trainingSet#se hace uso de la variable global
        clases = []#arreglo que guardara las clases que se encuentren
        with open(archivo, newline='') as csvfile:#se abre archivo
            lines = csv.reader(csvfile, delimiter= ';')#se hace la lectura
            dataset = list(lines)#se lista la lectura del dataset
            for x in range(len(dataset)-1):#recorrido del dataset
                for y in range(13):#limite de caracteristica de recorrido
                    dataset[x][y] = float(dataset[x][y])#se convierte de string a float
                clase = dataset[x][14]#se obtiene la clase
                if(x == 0):#por default la primera clase se guarda
                    clases.append(clase)#se inserta en el array clases
                if((clase in clases) == False):#se busca que no este la clase en el arreglo clases
                    clases.append(clase)#si no esta, se inserta
                trainingSet.append(dataset[x])#se reescribe el dataset con valores float
        csvfile.close()#se cierra la lectura
        print(Fore.RED+"  -------------------------------------------------------")
        print(Fore.BLUE+"          Información general")
        print(Fore.BLACK+"  Caracteristicas obtenidas: "+Fore.BLUE+"14")
        print(Fore.BLACK+"  Clases: "+Fore.BLUE)
        i = 0#se decalara contador        
        for clas in clases:#foreach para recorrer el array clases
            print("  "+str(clas)+", ",end='')#se imprime la clase
            if(i%5 == 0):#cada 5 calses da un salto de linea
                print('')#salto de linea
            i += 1#incrementa contado
        print(Fore.BLACK+"  Total de clases: "+Fore.BLUE+str(len(clases)))
        print(Fore.BLACK+"  Numero TOTAL de instancias: "+Fore.BLUE+ str(len(dataset)))
        print(Fore.RED+"  -------------------------------------------------------")

    """
        * Método euclidianDistance
        * Parametros: instanciaNueva, instanciaDataset, #caracteristicas
        * Retorna: distancia entre las dos instancias ingresadas
        * Funcionamiento:
        *  Mide la distancia euclidiana entre las dos instancias de entrada
    """
    def euclideanDistance(instance1, instance2, length):
        distance = 0#variable que guardara la distancia
        for x in range(length):#for que recorre las caracteriticas que requerimos
            distance += pow((instance1[x] - instance2[x]), 2)#se hacen operaciones
        return math.sqrt(distance)#se devuelve la raiz del calculo de la distancia
    """
        * Método: getNeighbors
        * Parametros: dataset, numero k
        * Retorna: los k vecinos
        * Funcionamiento:
        *  Mide la distancia de la nueva instancia con todo el dataset, guarda en un arreglo los k vecinos mas cercanos
    """
    def getNeighbors(testInstance, k):
        global trainingSet#se usa dataset
        distances = []#arreglo que guardara las distancias
        length = len(testInstance)-1#numero de caracteristicas
        for x in range(len(trainingSet)):#for que recorre el dataset
            dist = knn.euclideanDistance(testInstance, trainingSet[x], length)#se mide distancia
            distances.append((trainingSet[x], dist))#se inserta instancia con su distancia
        distances.sort(key=operator.itemgetter(1))#ordena de menor a mayor
        neighbors = []#arreglo de los k vecinos mas cercanos
        print(Fore.RED+"  -------------------------------------------------------")
        print(Fore.BLUE+"  K vecino  "+" Linea(Instancia) "+ " Clase: "+" Distancia: ")
        for x in range(k):#recorrido hasta numero k
            print(Fore.BLACK+"  "+str(x+1)+"              "+str(distances[x][0][15])+"           "+str(distances[x][0][14])+"       "+"%.5f" % round(distances[x][1],2))
            neighbors.append(distances[x][0])#se insertan los k vecinos mas cercanos
        return neighbors#se retornan los k vecinos mas cercanos
    """
        * Método: getResponse
        * Parametros: k vecinos mas cercanos
        * Retorna: la clase mayor
        * Funcionamiento:
        *  Cuenta que clase esta más veces
    """
    def getResponse(neighbors):
        classVotes = {}#diccionario que guardara las clases y sus cuentas
        print(Fore.RED+"  -------------------------------------------------------")
        print(Fore.BLUE+"\n       Resumen KNN")
        print("\n  Instancias de la clase   Votación")
        for x in range(len(neighbors)):#recorre los vecinos
            response = neighbors[x][-2]#obtiene la clase
            if response in classVotes:#busca si esta en
                classVotes[response] += 1#incrementa contador
            else:
                classVotes[response] = 1#incrementa contador
        for keys,values in classVotes.items():#recorrido para las impresiones
            print("         "+Fore.BLACK+str(keys)+Fore.BLUE+"                "+str(values))
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)#ordena el diccionario de mayor a menor
        return sortedVotes[0][0] #retorna la clase mayor

    """
        * Método: ObtenerCaract
        * Parametros: ruta de la img
        * Retorna: arreglo con las caracteristicas de la img
        * Funcionamiento:
        *  Obtiene las caracteristicas de la img
    """
    def obtenerCaract(self,ruta):
        data = []#se declara arreglo para guardar las caaracteristicas
        img = Image.open(ruta) #Abre imagne
        img2 = mpimg.imread(ruta) #Abre imagen
        columnas, filas = img.size #Se obtienen las filas y columnas

        #Se insertan datos en el array data
        data.extend(CreaData.arraysImg(img2,filas,columnas))#se inserta caracteristicas
        data.extend(CreaData.cortes(img2,filas,columnas))#se insertan caracteristicas
        #print(CreaData.cortes(img2,filas,columnas))
        data.append(CreaData.razonImagen(columnas,filas))#se insertan caracteristicas
        data.append(CreaData.razon_1s_area(columnas,filas,img2))#se insertan caracteristicas
        return data#retorna las caracteristicas
    """
        * Método: __init__
        * Parametros: No Aplica
        * Retorna: No Aplica
        * Funcionamiento:
        *  Constructor del objeto
    """
    def __init__(self):
        pass
    """
        * Método:  main
        * Parametros: No Aplica
        * Retorna: No Aplica
        * Funcionamiento:
        *  Controla la ejecucion del programa
    """
    def main(self):
        global trainingSet#usa la variable global
        data =[]#donde se guardaran las caract de la nueva img
        knn.cargarDataset('dataset2.csv')#carga el dataset
        input(Fore.BLACK+"  Se finalizo la carga de dataset, presione ENTER para continuar... : ")
        ruta = 'C:/Users/Paul/Desktop/OCR/ocrP/test/'
        ruta += input("  Ingresa el nombre de la imagen: ")#pide el nombre de la img
        data = knn.obtenerCaract(self,ruta)#obtiene caract de la img
        k = int(input("  Ingresa el numero K: "))#pide el numero k
        resultado = knn.getResponse(knn.getNeighbors(data,k))#se realiza la clasificacion
        print(Fore.BLACK+"\n       "+Back.CYAN+"LA IMAGEN ES UN:"+Back.RESET+Fore.RED+" "+str(resultado) +"  <-----")
        #print(len(trainingSet))
        del trainingSet[:]#elimina el dataset
        #print(len(trainingSet))
        
        
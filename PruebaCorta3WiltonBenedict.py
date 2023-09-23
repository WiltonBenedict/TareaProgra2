#8/2023. Wilton Benedict
#UH. Prueba Corta 3. sistema que ordene 2 arreglos que estan vinculados de un tamaño de 5 posiciones 
#Prueba Original 

#BLOQUE INICIAL
#######################

###
##Procedimiento que simplemente declara los arreglos y sus datos a usar
def Inicio1():
    #El inicio 1 simplemente declara los datos dentro del arreglo de forma predeterminada para probar la ordenacion.
    edades=[5,3,1,4,2]
    cedulas=[40,10,30,20,50]
    
    Menu(edades,cedulas)
###

##
def Inicio2():
    edades=[]
    cedulas=[]
    #contador utilizado como limite del ciclo
    cont1=int(input("Ingrese la cantidad de datos: "))
    #contador que acumula los ciclos
    cont2=1
    #contador que funciona como guia para insertar los datos en el indice
    cont3=0
    while(cont2<=cont1):
        #obtiene un valor temporal de la edad
        edad=int(input("Ingrese la edad "+str(cont2)+": "))
        #lo inserta de acuerdo al indice en el arreglo. Si el contador es 0, lo inserta en el indice 0.
        edades.insert(cont3, edad)
        #se repite el proceso pero con la cedula
        cedula=int(input("Ingrese la cedula "+str(cont2)+": "))
        cedulas.insert(cont3, cedula)
        #se actualiza el contador
        cont2+=1
        cont3+=1
    #una vez finalizado el ciclo, se llama al Menu y se envian los arreglos
    Menu(edades,cedulas)
##

def InicioPrincipal():
    #el objetivo de este procedimiento es determinar como el arreglo sera hecho.
    #Se pueden usar los datos predeterminados que estaba en moodle o utilizar datos propios con las longitudes propias de igual manera
    estado=True
    while(estado):
        print("Tipo de inicio")
        print("1. Usar datos predeterminados")
        print("2. Entrar datos propios")
        opc=int(input("Seleccion: "))
        if(opc==1):
            Inicio1()
            estado=False
        elif(opc==2):
            Inicio2()
            estado=False
        else:
            print("Seleccion invalida")

###
def Menu(edades,cedulas):
    estado=True
    while(estado):
        print("1. Ordenar por Edad")
        print("2. Ordenar por Cedula")
        print("3. Imprimir Lista")
        print("4. Salida")
        opc=int(input("Ingrese su seleccion: "))
        if(opc==1):
            #Dirige a solo ordenar el arreglo por orden de Edad de mayor a menor
            print("Ordenando por orden de Edad...")
            OrdenarEdad(edades,cedulas)
        elif(opc==2):
            #Dirige a solo ordenar el arreglo por orden de cedula de mayor a menor
            print("Ordenando por orden de Cedula...")
            OrdenarCedula(edades,cedulas)
        elif(opc==3):
            #Imprime la lista actual
            Imprimir(edades,cedulas)
        elif(opc==4):
            #termina el programa
            print("Saliendo...")
            estado=False
        else:
            #en caso que un dato incorrecto se ingrese, refiere de vuelta desde cero
            print("Seleccion Invalida")
###

#######################


#BLOQUE ORDEN y IMPRESION
#######################

###
def OrdenarCedula(edades,cedulas):
    #Menu para ordenar la lista sea de mayor a menor o menor a mayor
    estado=True
    while(estado):
        #hay dos tipos de ordenamiento. Mayor a menor y menor a mayor
        #lo unico que cambia es el operador < y >
        print("1. Ordenar de mayor a menor")
        print("2. Ordenar de menor a mayor")
        #se solicita como se desea organizar el dato
        opc=int(input("Ingrese su seleccion: "))
        if(opc==1):
            cont1=0
            #el ciclo usa de referencia el indice. Debido a esto el contador empieza desde cero y se resta un 1 a la cantidad total
            #para que concida con los indices
            while(cont1<(len(cedulas)-1)):
                cont2=cont1+1
                while(cont2<len(cedulas)):
                    #estructura selectiva que organizar de mayor a menor
                    if(cedulas[cont1]<cedulas[cont2]):
                        #en caso que corresponda, se ordenan ambos arreglos de acuerdo a su posicion
                        #se copia la posicion de ambos arreglos en dos varialbes
                        temp1=cedulas[cont1]
                        temp2=edades[cont1]
                        #se asigna nuevamente los datos. 
                        cedulas[cont1]=cedulas[cont2]
                        edades[cont1]=edades[cont2]
                        cedulas[cont2]=temp1
                        edades[cont2]=temp2
                    cont2+=1
                cont1+=1
                estado=False
            print("Ordenando por cedula de mayor a menor")
        elif(opc==2):
            cont1=0
            #exactamente lo mismo con el anterior pero ordenar de menor a mayor
            while(cont1<(len(cedulas)-1)):
                cont2=cont1+1
                while(cont2<len(cedulas)):
                    if(cedulas[cont1]>cedulas[cont2]):
                        temp1=cedulas[cont1]
                        temp2=edades[cont1]
                        cedulas[cont1]=cedulas[cont2]
                        edades[cont1]=edades[cont2]
                        cedulas[cont2]=temp1
                        edades[cont2]=temp2
                    cont2+=1
                cont1+=1
                estado=False
            print("Ordenando por cedula de menor a mayor")
        else:
            print("Seleccion invalida")
###

###
def OrdenarEdad(edades,cedulas):
    estado=True
    while(estado):
        #utiliza la misma organizacion que el de ordenar Cedual. Sin embargo lo que cambia es la estrucutra de repetiva
        print("1. Ordenar de mayor a menor")
        print("2. Ordenar de menor a mayor")
        opc=int(input("Ingrese su seleccion: "))
        if(opc==1):
            cont1=0
            #en la estructura repetitiva se utiliza mas bien las edades como punto de comparación
            while(cont1<(len(edades)-1)):
                cont2=cont1+1
                while(cont2<len(edades)):
                    if(edades[cont1]<edades[cont2]):
                        temp1=edades[cont1]
                        temp2=cedulas[cont1]
                        edades[cont1]=edades[cont2]
                        cedulas[cont1]=cedulas[cont2]
                        edades[cont2]=temp1
                        cedulas[cont2]=temp2
                    cont2+=1
                cont1+=1
                estado=False
            print("Ordenando por edad de mayor a menor")
        elif(opc==2):
            cont1=0
            while(cont1<(len(edades)-1)):
                cont2=cont1+1
                while(cont2<len(edades)):
                    if(edades[cont1]>edades[cont2]):
                        temp1=edades[cont1]
                        temp2=cedulas[cont1]
                        edades[cont1]=edades[cont2]
                        cedulas[cont1]=cedulas[cont2]
                        edades[cont2]=temp1
                        cedulas[cont2]=temp2
                    cont2+=1
                cont1+=1
                estado=False
            print("Ordenando por edad de menor a mayor")
        else:
            print("Seleccion invalida")
###

###
def Imprimir(edades,cedulas):
    #Utiliza for para imprimir tanto las edades como las cedulas
    cont=0
    print("Imprimiendo lista...")
    for x in edades:
        print("Edad:",x,"- Cedula: ",cedulas[cont])
        cont+=1
###

#######################

InicioPrincipal()

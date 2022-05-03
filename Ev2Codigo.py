#Se inician los modulos de import que se utilizaran para la realizacion de la evidenciafrom typing_extensions import Self
from tabulate import  tabulate
from collections import namedtuple
import csv

Lista = []

#Variable para registro
def RegistroSer():
    while True:
        #Recoleccion de datos de usuario
        NombreEquipo=input("Equipo/s a registrar: ")
        DetallesEquipo=input("Describe los detalles del equipo: ")
        FolioEquipo=input("Introduce el folio: ")
        FechaRegistro=input("Introduce la fecha de registro (dd/mm/aa): ")
        NombreCliente=input("Nombre del cliente: ")
        MontoCobrado= float (input("Monto cobrado : "))
        #Se calcula el IVA
        iva = MontoCobrado * 0.16

#Después de insertar los datos, se crea una lista donde se conservan para la impresión de los detalles del registro
# Luego de ingresar datos, se inicia una lista
        Registro = (NombreEquipo, DetallesEquipo, FolioEquipo, FechaRegistro, NombreCliente, MontoCobrado + iva)
        print ("_______________________Detalles_____________________")
        print ("Equipo/s: ", Registro[0])
        print ("Detalles equipo/s: ", Registro[1])
        print ("Folio del registro: ", Registro[2])
        print ("Fecha registro: ", Registro[3])
        print ("Nombre del cliente: ", Registro[4])
        print ("Precio total: $", Registro[5])

#Porcentaje de IVA cobrado a cliente
        print (f"(Aviso: el IVA de su monto es(16%): $", iva)

#Comenzamos a crear una tupla en la que irán los datos registrados a guardar en csv
Detelles = namedtuple( "Registro","Equipo, Detalles, Fecha, Cliente, Precio")
DatosAGrabar = dict()
Registro1 = Detelles("Laptop", "Cambio de tecleado retroiluminado", "4 Junio 2017",  "Jesus", 1500)
DatosAGrabar[1, 580] = Registro1

#Abrimos el archivo en modo escritura y para su grabacion
ArchGrab = open("RegistrosSoporte.csv","w", newline="")
Grabacion = csv.writer(ArchGrab)

#Titulo de CSV
Grabacion.writerow(("Clave, Precio", "Equipo", "Detalles", "Fecha", "Cliente"))

#Se graban datos y cierra CSV
Grabacion.writerow([(ClaveProducto, Informacion.Equipo, Informacion.Detalles, Informacion.Fecha, Informacion.Cliente) for ClaveProducto, Informacion in DatosAGrabar.items()])
ArchGrab.close()

#Variable con la cual se puede consultar con el folio lo que se hizo en el soporte
def ConsultaServ():
    while True:
        FolioNumero=input("Introduce el folio del servicio a consultar (dd/mm/aa):")
#Si el dato insertado es un folio anteriormente registrado y que se encuentre en la lista principal,
#se procede a imprimir y tabular el servicio consultado
        if FolioNumero==(Lista[2]):
            Conslta2 = [[Lista]]
        print(tabulate(Conslta2))
        break

#Se crea variable y se le consulta al Usuario la fecha
def FechaServ():
    while True:

#Si hay más de un servicio con la misma fecha, también se consultarán
#Al igual que la consulta con folio, la fecha también debe de estar dentro de la lista principal
#para que se pueda realizar la consulta
        FechaConsulta=input("Introduce la fecha del servicio que desee consultar (dd/mm/aa): ")
        if FechaConsulta==(Lista[3]):
            Cnslta = [[Lista]]
        print(tabulate(Cnslta))
        break

#Menu de opciones para la comodidad del usuario
while True:
    print(" ")
    print("_"*40)
    print("Servicio de soporte técnico")
    print("_"*40)
    print("[1] Registrar un servicio")
    print("[2] Consultar un servicio")
    print("[3] Consultar los servicios realizados en una fecha específica")
    print("[x] Salir")
    opcion=input("Qué opción deseas utilizar: ")
    if (opcion=="x"):
        break
    if (opcion=="1"):
        RegistroSer()
    if (opcion=="2"):
        ConsultaServ()
    if (opcion=="3"):
        FechaServ()


#Esperemos que la evidencia sea de su agrado :)
#Jesus Rodriguez
#Julian Emiliano
#Carlos Eduardo
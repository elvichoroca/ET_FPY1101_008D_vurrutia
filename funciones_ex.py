import random
import csv
def menu(titulo,lista):
    print('========================================')
    print(titulo.upper())
    print('========================================')
    while True:
        i=1
        for elem in lista:
            print(i,'.-',elem)
            i+=1
        print(i,'.- Salir')
        opc=input('Ingrese Opción: ')
        if opc.isdigit():
            opc_int=int(opc)
            if opc_int>=1 and opc_int<=i:
                return opc_int
            else:
                print('Debe Ingresar un Número entre 1 y ',i)
        else:
            print('Ingrese Sólo Números')

def sueldos_aleat(nom):
    sueldos=[]
    for i in range(10):
        nume=random.randrange(300000,2500000)
        sueldos.append(nume)
    trabaj=list(zip(nom,sueldos))  
    return trabaj

trabaj = ["Juan Pérez     ","María García   ","Carlos López   ","Ana Martínez   ","Pedro Rodríguez","Laura Hernández","Miguel Sánchez ","Isabel Gómez   ","Francisco Díaz " ,"Elena Fernández"]
suel_emple=sueldos_aleat(trabaj)

def reporte_de_sueldos():
    formato = input("Seleccione el formato del informe (csv): ").lower()
    if formato == 'csv':
        with open('reporte_de_sueldos.csv', 'w', newline='') as csvfile:
            fieldnames = ['Nombre empleado ', '', 'Descuento Salud', 'Descuento AFP', 'Sueldo liquido']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        print("Informe generado en formato CSV.")
    else:
        print("Formato no soportado.")


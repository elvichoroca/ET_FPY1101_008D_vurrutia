import funciones_ex as f
import random
while True:
    opc=f.menu('Menu principal',['Asignar sueldos aleatorios','Clasificar sueldos','Ver estadisticas','Reporte de sueldos'])
    if opc==1:
        print(f.suel_emple)
    elif opc==2:  
        print("Sueldos a menores a $800.000:")
        print("Nombre             Sueldo")
        for nom, sueldo in f.suel_emple:
            if sueldo<800000:
                print(f"{nom}  : {sueldo}")
        print("Sueldos entre $800.000 y $2.000.000")
        print("Nombre             Sueldo")
        for nom, sueldo in f.suel_emple:
            if sueldo>=800000 and sueldo<=2000000:
                print(f"{nom}  : {sueldo}")
        print("Sueldos superiores a $2.000.000")
        print("Nombre             Sueldo")
        for nom, sueldo in f.suel_emple:
            if sueldo>2000000:
                print(f"{nom}  : {sueldo}")          
        print("TOTAL SUELDOS: $",sueldo)         
    elif opc==3:    
        break
    elif opc==4:   
        print("Empleado         Sueldo Base     Descuento Salud        Descuento AFP       Sueldo liquido")
        for nom, sueldo in f.suel_emple:
            print(f"{nom}  : {sueldo}    /   {sueldo*0.07}           // {sueldo*0.12}   ///  {sueldo*0.81}")
    else:
        print("Finalizando programa...")
        print('Desarrollado por Vicente Urrutia')    
        print("Rut 21.900.399-4")
        break
   
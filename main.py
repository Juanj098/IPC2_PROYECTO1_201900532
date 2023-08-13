import os
import xml.etree.ElementTree as ET

os.system('cls')

# xml
def lector_xml(Docs_xml):
    tree = ET.parse(Docs_xml)
    root = tree.getroot()


print('<---------------------->')
print('-    MENU PRINCIPAL    -')
print('-1.CARGAR ARCHIVO      -')
print('-2.PROCESAR ARCHIVO    -')
print('-3.ESCRIBIR ARCHIVO S. -')
print('-4.DATOS ESTUDIANTE    -')
print('-5.GENERAR GRAFICA     -')
print('-6.INICIALIZAR SISTEMA -')
print('------------------------')
print('-       (x) SALIR      -')
print('<---------------------->')
opc = input('-> ')
os.system('cls')
while opc != 'x':
    global Doc_xml
    if opc == '1':
        print('cargar archivo :)')
        Doc_xml = input('Ingrese nombre del archivo: ')
        lector_xml(Doc_xml)
        os.system('cls')
    elif opc == '2':
        print('Procesar archivo')
    elif opc == '3':
        print('Escribir archivo salida')
    elif opc == '4':
        os.system('cls')
        opc_4 = ''
        while opc_4 != 'x':
            print('<----------------Datos estudiante---------------->')
            print('<  Juan Jose Gerardi Hernandez                   >')
            print('<  201900532                                     >')
            print('<  Introduccion a la Programacion 2 seccion D    >')
            print('<  Ingenieria en ciencias y sistemas             >')
            print('<  Sexto Semestre                                >')
            print('<------------------------------------------------>')
            print('<                   (x) Salir                    >')
            print('<------------------------------------------------>')
            opc_4 = input('-> ')
            os.system('cls')
    elif opc == '5':
        print('Generar grafica')
    elif opc == '6':
        print('iniciar sistema')
    elif opc == 'x':
        print('Salida')
    else:
        print('OPCION NO DISPONIBLE')
    print('<---------------------->')
    print('-    MENU PRINCIPAL    -')
    print('-1.CARGAR ARCHIVO      -')
    print('-2.PROCESAR ARCHIVO    -')
    print('-3.ESCRIBIR ARCHIVO S. -')
    print('-4.DATOS ESTUDIANTE    -')
    print('-5.GENERAR GRAFICA     -')
    print('-6.INICIALIZAR SISTEMA -')
    print('------------------------')
    print('-       (x) SALIR      -')
    print('<---------------------->')
    opc = input('-> ')    
    os.system('cls')
from tkinter.filedialog import askopenfile
import os
import xml.etree.ElementTree as ET
from list_senals import List_senal
from list_Data import List_Datos
from senales import Senal, Dato

list_datos = List_Datos()
list_sen = List_senal()
os.system('cls')

# xml
def lector_xml(Docs_xml):
    try:
        tree = ET.parse(Docs_xml)
        root = tree.getroot()
        for senales in root.findall('senal'):
            name = senales.get('nombre')
            t = senales.get('t')
            a = senales.get('A')
            for dato in senales.findall('dato'):
                tim = dato.get('t')
                amp = dato.get('A')
                dat = dato.text
                if int(dat)>0:
                    st = '1'
                elif str(dat) == '0':
                    st = '0'
                new_dato = Dato(tim,amp,st,dat)
                list_datos.new(new_dato)
            new_senal = Senal(name,t,a,list_datos)
            list_sen.new(new_senal)
    except:
        print('Archivo no encontrado!')

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
        Doc_xml = askopenfile(title='Buscar archivo XML',filetypes=(('archivos.xml','*.xml'),('Todos los archivos','*.*')))
        if Doc_xml:
            ruta = Doc_xml.name
            name = os.path.basename(ruta)
            print(name)
            lector_xml(ruta)
        else:
            print('no se encontro archivo')
    elif opc == '2':
        print('Procesar archivo')
        list_sen.enlist()
        list_sen.enlist_d()
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
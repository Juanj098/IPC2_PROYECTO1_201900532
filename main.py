from tkinter.filedialog import askopenfile
import os
import xml.etree.ElementTree as ET
from list_senals import List_senal
from list_Data import List_Datos
from senales import Senal, Dato
from list_iden import List_Identicos

list_i = List_Identicos()
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
                list_datos.insert_dato_ordenado(new_dato)
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
            list_sen.enlist_d()
        else:
            print('no se encontro archivo')
    elif opc == '2':
        print('Procesar Archivo')
        print('<-------------------------->')
        list_sen.enlist()
        print('<------------------------->')
        print('             (x)           ')
        print('<------------------------->')
        sen = input(' -> ')
        res = list_sen.search_sen(sen)
        os.system('cls')
        while sen != 'x':
            if res:
                print('<------------------------>')
                print('1. Matriz de Frecuecias   ')
                print('2. Matriz de patrones     ')
                print('3. Matriz reducida        ')
                print('<------------------------>')
                print('           (x)            ')
                print('<------------------------>')
                r = input('-> ')
                while r != 'x':
                    if r == '1':
                        os.system('cls')
                        print('Matriz de frecuencias')
                        res.matriz_frec()
                    elif r == '2':
                        os.system('cls')
                        print('Matriz de patrones')
                        res.matriz_Pa()
                    elif r == '3':
                        os.system('cls')
                        print('matriz Reducida')
                        res.matriz_re()
                    else:
                        print('Opcion no valida')
                    print('<------------------------>')
                    print('1. Matriz de Frecuecias   ')
                    print('2. Matriz de patrones     ')
                    print('3. Matriz reducida        ')
                    print('<------------------------>')
                    print('           (x)            ')
                    print('<------------------------>')
                    r = input('-> ')
                    os.system('cls')
            else:
                print('opcion no valida')
            print('<-------------------------->')
            list_sen.enlist()
            print('<------------------------->')
            print('             (x)           ')
            print('<------------------------->')
            sen = input(' -> ')
            os.system('cls')
    elif opc == '3':
        print('Escribir archivo salida')
        print('<------------------------->')
        list_sen.enlist()
        print('<------------------------->')
        print('            (x)            ')
        print('<------------------------->')
        DocX = input('-> ')
        busqueda = list_sen.search_sen(DocX)
        os.system('cls')
        while DocX != 'x':
            if busqueda:
                busqueda.Xml_salida()
            else:
                print('Error!')
            print('<------------------------->')
            list_sen.enlist()
            print('<------------------------->')
            print('            (x)            ')
            print('<------------------------->')
            DocX = input('-> ')
            os.system('cls')

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
        print('<----------------------->')
        list_sen.enlist()
        print('<----------------------->')
        print('           (x)           ')
        print('<----------------------->')
        z = input(' -> ')
        resp = list_sen.search_sen(z)
        os.system('cls')
        while z != 'x':
            if resp:
                print('<----------------------->')
                print('1.Grafica Frecuencias    ')
                print('2.Grafica Grupos         ')
                print('<----------------------->')
                print('           (x)           ')
                print('<----------------------->')
                graf = input('-> ')
                os.system('cls')
                while graf != 'x':
                    if graf == '1':
                        os.system('cls')
                        print('Grafica de Frecuencias')
                        resp.Graph_fr()
                    elif graf == '2':
                        os.system('cls')
                        print('Grafica de Grupos')
                        resp.Graph_re()
                    else:
                        os.system('cls')
                        print('Opcion no valida')
                    print('<----------------------->')
                    print('1.Grafica Frecuencias    ')
                    print('2.Grafica Grupos         ')
                    print('<----------------------->')
                    print('           (x)           ')
                    print('<----------------------->')
                    graf = input('-> ')
                    os.system('cls')
            else:
                print('Opcion no valida')
            print('<----------------------->')
            list_sen.enlist()
            print('<----------------------->')
            print('           (x)           ')
            print('<----------------------->')
            z = input(' -> ')
            os.system('cls')
    elif opc == '6':
        print('iniciar sistema')
        print('<----------------------------------------->')
        print('  Seguro que desea reiniciar sistema? S/N  ')
        print('<----------------------------------------->')
        print('                    (X)                    ')
        print('<----------------------------------------->')
        SN = input('-> ') 
        os.system('cls')
        while SN != 'N' and SN != 'x':
            if SN == 'S':
                os.system('cls')
                print('REINICIO')
                list_sen.Clear_list()
            else:
                os.system('cls')
                print('Opcion no disponible')
            print('<----------------------------------------->')
            print('  Seguro que desea reiniciar sistema? S/N  ')
            print('<----------------------------------------->')
            print('                    (X)                    ')
            print('<----------------------------------------->')

            SN = input('-> ') 
            os.system('cls')
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
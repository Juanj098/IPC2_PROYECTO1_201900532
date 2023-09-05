import xml.etree.ElementTree as ET 
from Nums import List_Nums
from groups import Suma

list_n = List_Nums()

class Nodo:
    def __init__(self,dato) -> None:
        self.dato = dato
        self.next = None

class List_Identicos:
    def __init__(self) -> None:
        self.init = None
        self.len = 0

    def vacia(self):
        if self.init == None:
            return True

    def New_gr(self,dato):
        new_Nodo = Nodo(dato)
        if self.vacia():
            self.init = new_Nodo
        else:
            aux = self.init
            while aux.next:
                aux = aux.next
            aux.next = new_Nodo
        self.len+=1

    def enlist(self):
        if self.vacia():
            print ('Lista vacia')
        else:
            aux = self.init
            while aux:
                print(aux.dato.prnt())
                aux =aux.next

    def ret_dato(self,mtx):
        if self.vacia():
            print ('Lista vacia')
        else:
            aux = self.init
            while aux:
                fun = self.Analizar(aux.dato.list,aux.dato.Grupos,aux.dato.len)
                mtx += fun
                aux =aux.next
        return mtx

    def Analizar(self,cadena,grupo,lenar):
        cadena = '/'+cadena
        mtx = ''
        puntero = 0
        dig = ''
        while puntero < len(cadena):
            digit = cadena[puntero]
            if digit == ';':
                digit = ''
            dig += digit            
            puntero+=1
        mtx += '\t\t<tr>\n'
        mtx += f'\t\t\t<td>G: {grupo}</td>\n'
        fun = self.Analizar_II(dig,grupo,int(lenar),mtx)
        return fun

    def Analizar_II(self,cadena, grupos,lenarr,mtx):
        suma = 0
        puntero = 0
        cade = ''
        lenarr = lenarr-1
        while puntero < len(cadena):
            char = cadena[puntero]
            if char == '/':
                if (puntero + 1) < len(cadena) and cadena[puntero + 1].isdigit():
                    dig = int(cadena[puntero + 1])
                    suma += dig
                    cade += char
                    puntero += 1  # Saltar al siguiente dígito
                else:
                    mtx += f'\t\t\t<td>{suma}</td>\n'
                    cade += char
            else:
                cade += char
            puntero += 1
        if cade[1] != '/':
            return self.Analizar_II(cade,grupos,lenarr,mtx)
        else:
            mtx+='\t\t</tr>\n'
            return mtx

    def graficar(self,mtx):
        dat = self.ret_dato(mtx)
        return dat

    
    def Proc(self,Grp,amp):
        if self.vacia():
            print ('Lista vacia')
        else:
            cont = 0
            aux = self.init
            while aux:
                fun = self.Graph(aux.dato.list,aux.dato.Grupos,cont,amp)
                cont+=1
                Grp+=fun
                aux =aux.next
        fun2 = self.nodes(amp,cont)
        Grp += fun2
        return Grp

    def Graph(self,cadena,grupo,cont,amp):
        ABC ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        cadena = '/'+cadena
        puntero = 0
        cont2 = 0
        dig = ''
        nodes = ''
        grp = ''
        while puntero < len(cadena):
            digit = cadena[puntero]
            if digit == ';':
                digit = ''
            dig += digit            
            puntero+=1
        nodes +=  f'\tNode{ABC[cont]}[label="G: {grupo}"]\n'
        fun = self.Sumatorias(dig,grupo,cont,grp,cont2)
        nodes += fun
        return nodes
    
    def Sumatorias(self,cadena,Grupo,cont,grp,cont2): 
        ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        puntero = 0
        dig = ''
        suma = 0
        cade = ''
        while puntero < len(cadena):
            char = cadena[puntero]
            if char == '/':
                if (puntero+1) < len(cadena) and cadena[puntero+1].isdigit():
                    dig = int(cadena[puntero + 1])
                    suma += dig
                    cade += char
                    puntero+=1
                else:
                    cont2 += 1
                    grp  += f'\tNode{ABC[cont]}{cont2}[label="{suma}"]\n'
                    cade+=char
            else:
                cade+=char
            puntero+=1
        if cade[1] != '/':
            return self.Sumatorias(cade,Grupo,cont,grp,cont2)
        else: 
            return grp

    def nodes(self,amp,cont):
        ABC = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        Canode = ''
        amp = int(amp)
        for x in range(amp+1):    
            for y in range(1,cont+1):
                if x == 0:
                    if y < cont:
                        if y == 1:
                            Canode += f'\tNode0 -> Node{ABC[y]} -> '
                        else:
                            Canode += f'Node{ABC[y]} -> '
                    else:
                        Canode += f'Node{ABC[y]}\n'
                else:
                    if y < cont:                    
                        if y == 1:
                            Canode += f'\tNode0 -> Node{ABC[y]}{int(x)} -> '
                        else:
                            Canode += f'Node{ABC[y]}{int(x)} ->'
                    else:
                        Canode += f'Node{ABC[y]}{int(x)}\n'
        return Canode
        

    def graficar_ii(self,Grp,amp):
        dat = self.Proc(Grp,amp)
        return dat
    
    
    def Xml_c(self,name,path,amp):
        cont = 0
        root = ET.Element('senalReducida')
        senal = ET.SubElement(root,'senal',nombre = name, A = amp)
        if self.vacia():
            print ('Lista vacia')
        else:
            aux = self.init
            while aux:
                cont +=1
                print(aux.dato.Grupos)
                grupos = ET.SubElement(senal,'Grupo', g = str(cont))
                tiempo = ET.SubElement(grupos,'tiempos')
                tiempo.text = str(aux.dato.Grupos)
                print(aux.dato.list)
                self.xml_Analisis(aux.dato.list,grupos,amp)
                aux = aux.next
        path = str(path)
        tree = ET.ElementTree(root)
        tree.write(path,encoding='utf-8')
    
    def xml_Analisis(self,cadena,sub,amp):
        cadena = '/'+cadena
        puntero = 0
        dig = ''
        sumAmp = 0
        digit = ''
        while puntero < len(cadena):
            digit = cadena[puntero]
            if digit == ';':
                digit = ''
            dig += digit
            puntero += 1
        datosG = ET.SubElement(sub,'datosGrupo')
        suma = self.Xml_suma(dig,sub,amp,datosG,sumAmp)
        if suma:
            suma_elm = ET.SubElement(datosG,'suma')
            suma_elm.text = str(suma)
            
    def Xml_suma(self,cadena,sub,amp,datosG,sumAmp):
        puntero = 0
        suma = 0
        dig = ''
        cade = ''
        while puntero < len(cadena):
            char = cadena[puntero]
            if char == '/':
                if (puntero + 1) < len(cadena) and cadena[puntero+1].isdigit():
                    dig = int(cadena[puntero + 1])
                    suma += dig
                    cade += char
                    puntero+=1
                else:
                    sumAmp+=1
                    ET.SubElement(datosG,'suma',A=str(sumAmp)).text = str(suma)
                    cade += char
            else:
                cade+=char
            puntero+=1
        if cade[1] != '/' :
            return self.Xml_suma(cade,sub,amp,datosG,sumAmp)



    def G_xml(self,path,name,amp):
        return self.Xml_c(name,path,amp)
 
        
        

        
        
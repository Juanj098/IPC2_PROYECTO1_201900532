from Nums import List_Nums
from groups import Nums

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


        
 
        
        

        
        
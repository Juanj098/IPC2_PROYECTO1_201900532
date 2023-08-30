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

    def ret_dato(self):
        if self.vacia():
            print ('Lista vacia')
        else:
            aux = self.init
            while aux:
                self.Analizar(aux.dato.list,aux.dato.Grupos,aux.dato.len)
                aux =aux.next
        

    def Analizar(self,cadena,grupo,lenar):
        cadena = '/'+cadena
        cont = 0
        puntero = 0
        while puntero < len(cadena):
            digit = cadena[puntero]
            if digit == ';':
                digit = ''
            elif digit == '/':
                cont = 0
            elif digit.isdigit():
                cont+=1
                # print(f'-{grupo}:{digit}:{cont}:len{lenar}')
                num = Nums(grupo,digit,cont)
                list_n.New_Num(num)
                # list_n.enlist()
            puntero+=1

   
    def graficar(self):
        graph = ''
        suma = 0
        if self.vacia():
            print('lista vacia')
        else:
            aux = self.init
            while aux:
                print(aux.dato.Grupos)
                print(f'len: {aux.dato.len}')
                aux = aux.next
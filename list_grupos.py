from list_iden import List_Identicos
from Nums import List_Nums

list_N = List_Nums()
list_i = List_Identicos()

class Iden:
    def __init__(self,grupos,lis,len) -> None:
        self.Grupos = grupos
        self.list = lis
        self.len = len

    def prnt(self):
        return f'Gr:{self.Grupos} list:{self.list}'

class Nodo:
    def __init__(self,dato) -> None:
        self.dato = dato
        self.next = None

class List_Grupos:
    def __init__(self) -> None:
        self.init = None
        self.len = 0

    def vacia(self):
        if self.init == None:
            return True

    def New_G(self,dato):
        nodo = Nodo(dato)
        if self.vacia():
            self.init = nodo
        else:
            aux = self.init
            while aux.next:
                aux = aux.next
            aux.next = nodo
        self.len+=1

    def vaciar(self):
        self.init = None
        
    def enlist(self):
        if self.vacia():
            return 'lista vacia'
        else:
            aux = self.init
            while aux:
                print(aux.dato.prnt())
                aux =aux.next

    def search_G(self,nG):
        if self.vacia():
            return 'Lista Vacia'
        else:
            aux = self.init
            while aux:
                if aux.dato.gr == (nG):
                    return aux.dato
                aux = aux.next
    
    def delete_D(self,dato):
        if self.vacia():
            return 'lista vacia'
        if self.init.dato.gr == dato:
            self.init = self.init.next
        else:
            prev = None
            aux = self.init
            while aux:
                if aux.dato.gr == dato:
                    prev.next = aux.next
                prev = aux
                aux = aux.next

    def Iguales(self):
        if self.vacia():
            return 'Lista Vacia'
        else:
            lis_da = ''
            groups = ''
            aux = self.init
            current = self.init.dato.patron
            while aux:
                if current == aux.dato.patron:
                    groups+=f'{aux.dato.gr} '
                    lis_da+=f'{aux.dato.list_d}/'
                    self.delete_D(aux.dato.gr)
                    len = aux.dato.len
                aux = aux.next
            print(f'GR: {groups} Datos: {lis_da}')
            dato = Iden(groups,lis_da,len)
            list_i.New_gr(dato)
        self.Iguales()
    
    def enlis_I(self,mtx):
        fun = list_i.graficar(mtx)
        if fun:
            return fun
        
    def Graph_re(self,Grp,amp):
        fun = list_i.graficar_ii(Grp,amp)
        if fun:
            return fun
        
    def Xml(self,path,name,amp):
        xm = list_i.G_xml(path,name,amp)
        return xm





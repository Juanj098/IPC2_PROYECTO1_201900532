class Nodo:
    def __init__(self,dato) -> None:
        self.next = None
        self.dato = dato

class List_senal:
    def __init__(self) -> None:
        self.init = None
        self.len = 0
    
    def vacia(self):
        if self.init is None:
            return True

    def new(self,dato):
        new_nodo = Nodo(dato)
        if self.vacia():
            self.init = new_nodo
        else:
            aux = self.init
            while aux.next:
                aux = aux.next
            aux.next = new_nodo
        self.len += 1

    def enlist(self):
        if self.vacia():
            print('Lista vacia') 
        else:
            aux = self.init
            while aux:
                print(aux.dato.prnt())
                aux = aux.next

    def enlist_d(self):
        if self.vacia():
            return 'Lista Vacia'
        else:
            aux = self.init
            while aux:
                print(aux.dato.prnt_L())
                aux = aux.next
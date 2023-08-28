class Nodo:
    def __init__(self,dato) -> None:
        self.dato = dato
        self.next = None

class linkedList:
    def __init__(self) -> None:
        self.init = None
        self.len = 0
    
    def vacia(self):
        if self.init is None:
            return True

    def New_D(self,dato):
        n_nodo = Nodo(dato)
        if self.vacia():
            self.init = n_nodo
        else:
            aux = self.init
            while aux.next:
                aux = aux.next
            aux.next = n_nodo
        self.len+=1
    
    def enlist(self):
        if self.vacia():
            print('lista vacia')
        else:
            aux = self.init
            while aux:
                print(aux.dato.prnt())
                aux = aux.next
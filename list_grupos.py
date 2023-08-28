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

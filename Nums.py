class Nodo:
    def __init__(self,dato) -> None:
        self.dato = dato
        self.next = None

class List_Nums:
    def __init__(self) -> None:
        self.init = None
        self.len = 0

    def vacia(self):
        if self.init == None:
            return True

    def New_Num(self,dato):
        node = Nodo(dato)
        if self.vacia:
            self.init = node
        else:
            aux = self.init
            while aux.next:
                aux = aux.next
            aux.next = node
        self.len+=1

    def enlist(self):
        if self.vacia():
            print('lista vacia')
        else:
            aux = self.init
            while aux:
                print(f'{aux.dato.prnt()}')
                aux = aux.next


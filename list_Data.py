class Nodo:
    def __init__(self,dato) -> None:
        self.next = None
        self.dato = dato

class List_Datos:
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
        self.len+=1
    
    def insert_dato_ordenado(self, dato):
        new_Nodo = Nodo(dato)
        self.len += 1
        # Si la lista está vacía solo añade el nuevo nodo
        if self.init is None:
            self.init = new_Nodo
            return
        # Caso especial: la nueva celda debe ser el nuevo primer nodo, debe reemplazar al primero
        if dato.ti < self.init.dato.ti or (dato.ti == self.init.dato.ti and dato.ampl <= self.init.dato.ampl):
            new_Nodo.next = self.init
            self.init = new_Nodo
            return
        # Si no cumple con ninguno de los casos, recorrer hasta encontrar su posición
        actual = self.init
        while actual.next is not None and (dato.ti > actual.next.dato.ti or (dato.ti == actual.next.dato.ti and dato.ampl > actual.next.dato.ampl)):
            actual = actual.next
        new_Nodo.next = actual.next
        actual.next = new_Nodo

    def new_ordenado(self,dato):
        nodo = Nodo(dato)
        if self.vacia:
            self.init = nodo
        elif self.init.next == None:
            if dato.ti < self.init.dato.ti:
                aux = self.init
                self.init = nodo
                self.init.next = aux
            elif self.init.dato.ti == dato.ti:
                if self.init.dato.ampl < dato.ampl:
                    self.init.next = nodo
                elif self.init.dato.ampl > dato.ampl:
                    aux = self.init
                    self.init = nodo
                    self.init.next = aux
        else:
            aux = self.init
            while aux.next:
                if (dato.ti == aux.dato.ti) and (aux == self.init):
                    if dato.ampl < aux.dato.ampl:
                        nodo.next = aux
                        self.init = nodo
                    elif (dato.ti > aux.dato.ti) and (dato.ti < aux.next.dato.ti):
                        ax = aux.next
                        aux.next = nodo
                        nodo.next = ax
                    elif (dato.ti == aux.dato.ti) and (dato.ti < aux.next.dato.ti):
                        if (dato.ampl > aux.dato.ampl):
                            current = aux.next
                            nodo.next = current
                            aux = nodo
                    elif (dato.ti > aux.dato.ti) and (dato.ti == aux.next.dato.ti):
                        if (dato.ampl < aux.next.dato.ampl):
                            current = aux.next
                            nodo.next = current
                            aux.next = nodo
                    elif (dato.ti == aux.dato.ti) and (dato.ti == aux.next.dato.ti):
                        if (dato.ampl > aux.dato.ampl) and (dato.ampl < aux.next.dato.ampl):
                            current = aux.next
                            nodo.next = current
                            aux.next = nodo
                    else:
                        aux.next = nodo
                aux = aux.next

    def enlist(self):
        if self.vacia():
            return 'Lista vacia'
        else:
            aux = self.init
            while aux:
                print(f'--{aux.dato.prnt()}')
                aux = aux.next
    
    def search_T(self,t,a):
        if self.vacia():
            print('Lista vacia')
        else:
            aux = self.init
            while aux:
                if aux.dato:
                    if aux.dato.ti == str(t) and aux.dato.ampl == str(a): 
                        return aux.dato
                aux = aux.next

    def search_A(self,a,t):
        if self.vacia():
            print('Lista vacia')
        else:
            aux = self.init
            while aux:
                if aux.dato:
                    if aux.dato.ti == str(t) and aux.dato.ampl == str(a): 
                        return aux.dato
                aux = aux.next
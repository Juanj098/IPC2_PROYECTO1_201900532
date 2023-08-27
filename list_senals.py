import os
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

    # def matriz_fr(self):
    #     mat = '''digraph main {
    #     node [shape = plaintext]
    #     struct1 [label=<
    #     <table border = '0' cellborder = '1' cellspacing = '0'>
    #     '''
    #     if self.vacia(): 
    #         return 'Lista vacia'
    #     else:
    #         aux = self.init
    #         while aux:
    #             if aux != None:
    #                 mat+='<tr>\n'
    #                 for s in range(int(aux.dato.amp)+1):
    #                     if s == 0:
    #                       mat+='\t\t<td bgcolor="red">t|A</td>\n'
    #                     else:
    #                         mat+=f'\t\t<td>  {s}</td>\n'
    #                 mat+='\t</tr>\n'  
    #                 for y in range(1,int(aux.dato.tiem)+1): #tiempo
    #                     mat+=f'\t<tr>\n\t\t<td>{y}</td>\n'
    #                     for x in range(1,int(aux.dato.amp)+1): #amplitud
    #                            resp = aux.dato.list.search_T(y,x)
    #                            if resp:
    #                                mat+=f'\t\t<td>{resp.dat}</td>\n'
    #                     mat+='\t</tr>\n'
    #             aux = aux.next
    #     mat+='\t</table>>];\n'            
    #     mat+='}'
    #     with open('matriz.dot','w',encoding='UTF-8') as Doc:
    #         Doc.write(mat)
    #         Doc.close()
    #     os.system("dot -Tpng Matriz_fr.dot -o Matriz_fr.png")
    def search_sen(self,senal):
        if self.vacia():
            return 'Lista Vacia'
        else:
            aux = self.init
            while aux:
                if aux.dato.name == senal:
                    return aux.dato
                aux = aux.next

    def matriz_pa(self,senal):
        pass

    def matriz_re(self,senal):
        pass



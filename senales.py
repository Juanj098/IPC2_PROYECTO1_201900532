import os

from linkedList import linkedList
linked = linkedList()
from list_grupos import List_Grupos
list_g = List_Grupos()
class Senal:
    def __init__(self,nombre,t,a,list) -> None:
        self .name = nombre
        self.amp = a
        self.tiem = t
        self.list = list

    def prnt(self):
        return f'N:{self.name}, t:{self.tiem}, A:{self.amp}'
    
    def prnt_L(self):
        return self.list.enlist()
    
    def matriz_frec(self):
        mat = '''digraph main {
        node [shape = plaintext]
        struct1 [label=<
        <table border = '0' cellborder = '1' cellspacing = '0'>
        '''
        mat+='<tr>\n'
        for s in range(int(self.amp)+1):
            if s == 0:
                mat+='\t\t<td bgcolor="red">t|A</td>\n'
            else:
                mat+=f'\t\t<td>   {s}</td>\n'
        mat+='\t</tr>\n'
        for y in range(1,int(self.tiem)+1): #tiempo
            mat+=f'\t<tr>\n\t\t<td>{y}</td>\n'
            for x in range(1,int(self.amp)+1): #amplitud
                resp = self.list.search_T(y,x)
                if resp:
                    mat+=f'\t\t<td>{resp.dat}</td>\n'
            mat+='\t</tr>\n'
        mat+='\t</table>>];\n'
        mat+='}'
        with open('matriz_fr.dot','w',encoding='UTF-8') as Doc:
            Doc.write(mat)
            Doc.close()
        os.system("dot -Tpng Matriz_fr.dot -o Matriz_fr.png")

    def matriz_Pa(self):
        mat = '''digraph main {
        node [shape = plaintext]
        struct1 [label=<
        <table border = '0' cellborder = '1' cellspacing = '0'>
        '''
        mat+='<tr>\n'
        for s in range(int(self.amp)+1):
            if s == 0:
                mat+='\t\t<td bgcolor="Green">t|A</td>\n'
            else:
                mat+=f'\t\t<td>   {s}</td>\n'
        mat+='\t</tr>\n'
        for y in range(1,int(self.tiem)+1): #tiempo
            mat+=f'\t<tr>\n\t\t<td>{y}</td>\n'
            for x in range(1,int(self.amp)+1): #amplitud
                resp = self.list.search_T(y,x)
                if resp:
                    mat+=f'\t\t<td>{resp.state}</td>\n'
            mat+='\t</tr>\n'
        mat+='\t</table>>];\n'
        mat+='}'
        with open('matriz_Pa.dot','w',encoding='UTF-8') as Doc:
            Doc.write(mat)
            Doc.close()
        os.system("dot -Tpng Matriz_Pa.dot -o Matriz_Pa.png")        

    def matriz_re(self):
        for y in range(1,int(self.tiem)+1):
            patron = ""
            for x in range(1,int(self.amp)+1):
                resp= self.list.search_T(y,x)
                if resp:
                    patron+=resp.state
                    linked.New_D(resp)
            gr = Grupos(y,patron,linked)
            list_g.New_G(gr)
        
        list_g.enlist()

class Dato:
    def __init__(self,t,a,st,dat) -> None:
        self.ti = t
        self.ampl = a
        self.state = st
        self.dat = dat

    def prnt(self):
        return f't:{self.ti}, A:{self.ampl}, State:{self.state}, D:{self.dat}'

class Grupos:
    def __init__(self,G,patron,list_d) -> None:
        self.gr = G
        self.patron = patron
        self.list_d = list_d

    def prnt(self):
        return f'Grupo: {self.gr}, Patron: {self.patron}'
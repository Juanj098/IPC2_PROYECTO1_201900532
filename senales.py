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
    
    def matriz_frec(self): #matriz de frecuencias
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

    def matriz_Pa(self): # matriz de patrones
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

    def matriz_re(self): #matriz reducida
        mtx = '''digraph main {
        node [shape = plaintext]
        struct1 [label=<
        <table border = '0' cellborder = '1' cellspacing = '0'>
        '''
        mtx += '<tr>\n'
        for r in range(int(self.amp)+1):
            if r == 0:
                mtx += '\t<td bgcolor="Green">t|A</td>\n'
            else:
                mtx += f'\t<td>{r}</td>\n'
        mtx += '\t</tr>\n'
        list_g.vaciar()
        for y in range(1,int(self.tiem)+1):
            patron = ''
            data = ''
            for x in range(1,int(self.amp)+1):
                resp= self.list.search_T(y,x)
                if resp:
                    patron+=resp.state
                    data+=resp.dat
                    if x <= int(self.amp):
                        data+=';'
            gr = Grupos(y,patron,data,self.amp)
            list_g.New_G(gr)

        ('------------')
        list_g.enlist()
        print('-------')
        list_g.Iguales()
        x = list_g.enlis_I(mtx)
        print('--------')
        x+='''\t</table>>];\n}'''
        with open('matriz_re.dot','w',encoding='UTF-8') as Doc:
            Doc.write(x)
            Doc.close()
        os.system("dot -Tpng Matriz_re.dot -o Matriz_re.png") 

class Dato:
    def __init__(self,t,a,st,dat) -> None:
        self.ti = t
        self.ampl = a
        self.state = st
        self.dat = dat

    def prnt(self):
        return f't:{self.ti}, A:{self.ampl}, State:{self.state}, D:{self.dat}'

class Grupos:
    def __init__(self,G,patron,datos,len) -> None:
        self.gr = G
        self.patron = patron
        self.list_d = datos
        self.len = len

    def prnt(self):
        return f'Grupo: {self.gr}, Patron: {self.patron} Elm: {self.list_d}'


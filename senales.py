import os
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


class Dato:
    def __init__(self,t,a,st,dat) -> None:
        self.ti = t
        self.ampl = a
        self.state = st
        self.dat = dat

    def prnt(self):
        return f't:{self.ti}, A:{self.ampl}, State:{self.state}, D:{self.dat}'

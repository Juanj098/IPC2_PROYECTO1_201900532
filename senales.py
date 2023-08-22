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
class Dato:
    def __init__(self,t,a,st,dat) -> None:
        self.ti = t
        self.ampl = a
        self.state = st
        self.dat = dat

    def prnt(self):
        return f't:{self.ti}, A:{self.ampl}, State:{self.state}, D:{self.dat}'

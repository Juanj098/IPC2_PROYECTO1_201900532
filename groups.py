    
class Nums:
    def __init__(self,grupo,dato,num) -> None:
        self.grupo = grupo
        self.dato = dato
        self.num = num

    def prnt(self):
        return f'grupo:{self.grupo}, dato:{self.dato}, num:{self.num}'
    
class Suma:
    def __init__(self,indice,sum) -> None:
        self.indice = indice
        self.sum = sum
    
    def prnt(self):
        return f'grupo:{self.indice}, dato:{self.sum}'

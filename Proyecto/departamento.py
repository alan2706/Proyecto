class Departamento:
    secuencia=0
    departamentos=[]
    
    def __init__(self,descrip):
        Departamento.secuencia +=1
        self.codigo=Departamento.secuencia
        self.departamentos=descrip
        
    def registro(self):
        return{"codigo":self.codigo,"departamento":self.departamentos}
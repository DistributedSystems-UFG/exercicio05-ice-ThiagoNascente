import sys, Ice, random

try:
    Ice.loadSlice('-I. Functions.ice') #on aws
except TypeError:
    Ice.loadSlice(['-I.', 'Functions.ice']) #local
import Demo
 
class FunctionsI(Demo.Functions):
    def __init__(self, nome):
        super().__init__()
        self.name = nome
        
    def registra(self, texto, current=None):
        print(f'{self.name} {texto}')
    
    def printString(self, s, current=None):
        self.registra(f' disse \'{s}\'')
        return f'mensagem [{s}] foi impressa por {self.name}'
    
    def cumprimentar(self, nome, current=None):
        self.registra(f'cumprimentou {nome}')
        return f'Olá {nome}! Espero que você esteja bem!'

    def inverter(self, texto, current=None):
        self.registra(f'inverteu {texto}')
        texto_invertido = texto[::-1]
        return f'{texto} -> invertido fica {texto_invertido}'
    
    def palindromo(self, texto, current=None):
        self.registra(f'verificou se {texto} é palíndromo')
        texto_invertido = texto[::-1]
        res = 'É'
        if texto != texto_invertido:
            res = 'Não é'
        return f'{texto} -> texto invertido fica {texto_invertido} -> {res} palindromo!'
        
    def rolarDado(self, numero, current=None):
        self.registra(f'rolou um dado d{numero}')
        num = int(numero)
        if num <= 0:
            return 'valor invalido!'
        res = random.randint(1, num)
        return f'resultado da rolagem do d{num}: {res}'
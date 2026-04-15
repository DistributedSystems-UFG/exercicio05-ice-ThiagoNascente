
import sys, Ice
import Demo
#from servants import FunctionsI

with Ice.initialize(sys.argv) as communicator:
    #host = 'localhost' #para localhost
    host = '172.31.37.241' #<ip_da_maquina_servidor>
    base = communicator.stringToProxy(f"SimpleFunctions:tcp -h {host} -p 5678")
    obj = Demo.FunctionsPrx.checkedCast(base)
    if not obj:
        raise RuntimeError("Invalid proxy")

    print(obj.printString("Hello World! Comunicacao feita com sucesso!!!"))
    nome = input('Digite seu nome: ')
    print(obj.cumprimentar(nome))
    texto = input('Entre com um texto para ser invertido: ')
    print(obj.inverter(texto))

import sys, Ice

Ice.loadSlice(['-I.', 'Functions.ice'])
import Demo
 
with Ice.initialize(sys.argv) as communicator:
    host = 'localhost' #para localhost
    #host = '' #<ip_da_maquina_servidor>
    base1 = communicator.stringToProxy(f"SimpleFunctions1:tcp -h {host} -p 5679")
    base2 = communicator.stringToProxy(f"SimpleFunctions2:tcp -h {host} -p 5679")
    obj1 = Demo.FunctionsPrx.checkedCast(base1)
    obj2 = Demo.FunctionsPrx.checkedCast(base2)
    if (not obj1) or (not obj2):
        raise RuntimeError("Invalid proxy")

    print(obj1.printString("Hello World from object1!"))
    texto = input('Entre com um texto: ')
    print(obj1.palindromo(texto))
    numero = input('Entre com um numero (numero de lados do seu dado): ')
    print(obj1.rolarDado(numero))
    
    print('---------------------------------')
    
    print(obj2.printString("Hello World from object2!"))
    texto = input('Entre com um texto: ')
    print(obj2.palindromo(texto))
    numero = input('Entre com um numero (numero de lados do seu dado): ')
    print(obj2.rolarDado(numero))

    #communicator.waitForShutdown() #Isso acontece so em arquivos do tipo servidor

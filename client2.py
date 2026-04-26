import sys, Ice
import Demo


def iniciar_cliente():
    host_remoto = '54.196.85.80'
    host_local = 'localhost'
    porta = '5679'
    
    try:
        with Ice.initialize(sys.argv) as communicator:
            obj1 = None
            obj2 = None
            try:
                # tentar no servidor Remoto
                print(f"Tentando conectar em {host_remoto}...")
                base1 = communicator.stringToProxy(f"SimpleFunctions1:tcp -h {host_remoto} -p {porta}")
                base2 = communicator.stringToProxy(f"SimpleFunctions2:tcp -h {host_remoto} -p {porta}")
                obj1 = Demo.FunctionsPrx.checkedCast(base1)
                obj2 = Demo.FunctionsPrx.checkedCast(base2)
                
            except (Ice.ConnectTimeoutException, Ice.ConnectionRefusedException):
                # tentar no servidor local
                try:
                    print("Servidor remoto offline. Tentando localhost...")
                    base1 = communicator.stringToProxy(f"SimpleFunctions1:tcp -h {host_local} -p {porta}")
                    base2 = communicator.stringToProxy(f"SimpleFunctions2:tcp -h {host_local} -p {porta}")
                    obj1 = Demo.FunctionsPrx.checkedCast(base1)
                    obj2 = Demo.FunctionsPrx.checkedCast(base2)
                except Ice.ConnectionRefusedException:
                    print("Erro: Nem o servidor remoto nem o local estão ativos.")
                    return

            if obj1 and obj2:
                executar_logica(obj1)
                print('--------------------------')
                executar_logica(obj2)
            else:
                print("Não foi possível estabelecer conexão com nenhum servidor.")
    except Ice.Exception as e:
        print(f"Erro inesperado no Ice: {e}")
    except Exception as e:
        print(f"Erro crítico no sistema: {e}")
        
def executar_logica(obj):
    print(obj.printString("Hello World!"))
    texto = input('Entre com um texto: ')
    print(obj.palindromo(texto))
    numero = input('Entre com um numero (numero de lados do seu dado): ')
    print(obj.rolarDado(numero))

if __name__ == "__main__":
    try:
        iniciar_cliente()
    except KeyboardInterrupt:
        print("\nSessão client2.py encerrada pelo usuario.")
        sys.exit(0)

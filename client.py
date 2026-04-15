import sys
import Ice
import Demo

def iniciar_cliente():
    host_remoto = '172.31.37.241'
    host_local = 'localhost'
    porta = '5678'
    
    try:
        with Ice.initialize(sys.argv) as communicator:
            obj = None
            
            try:
                # tentar no servidor Remoto
                print(f"Tentando conectar em {host_remoto}...")
                base = communicator.stringToProxy(f"SimpleFunctions:tcp -h {host_remoto} -p {porta}")
                obj = Demo.FunctionsPrx.checkedCast(base)
            except (Ice.ConnectTimeoutException, Ice.ConnectionRefusedException):
                # tentar no servidor Local
                try:
                    print("Servidor remoto offline. Tentando localhost...")
                    base = communicator.stringToProxy(f"SimpleFunctions:tcp -h {host_local} -p {porta}")
                    obj = Demo.FunctionsPrx.checkedCast(base)
                except Ice.ConnectionRefusedException:
                    print("Erro: Nem o servidor remoto nem o local estão ativos.")
                    return

            if obj:
                executar_logica(obj)
            else:
                print("Não foi possível estabelecer conexão com nenhum servidor.")

    except Ice.Exception as e:
        print(f"Erro inesperado no Ice: {e}")
    except Exception as e:
        print(f"Erro crítico no sistema: {e}")

def executar_logica(obj):
    
    print(obj.printString("Hello World! Comunicação feita com sucesso!!!"))
    
    nome = input('Digite seu nome: ')
    print(obj.cumprimentar(nome))
    
    texto = input('Entre com um texto para ser invertido: ')
    print(obj.inverter(texto))

if __name__ == "__main__":
    try:
        iniciar_cliente()
    except KeyboardInterrupt:
        print("\nSessão client.py encerrada pelo usuario.")
        sys.exit(0)
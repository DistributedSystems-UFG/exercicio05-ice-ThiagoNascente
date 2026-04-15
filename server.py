import sys, Ice
from servants import FunctionsI

def run():
    with Ice.initialize(sys.argv) as communicator:

        adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -h 0.0.0.0 -p 5678")
        object = FunctionsI('objeto')
        adapter.add(object, Ice.stringToIdentity("SimpleFunctions"))

        adapter.activate()
        print("Servidor rodando na porta 5678...")
        communicator.waitForShutdown()
        
if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print(f"\nServidor (server.py) encerrado por KeyboardInterrupt.")
        sys.exit(0)
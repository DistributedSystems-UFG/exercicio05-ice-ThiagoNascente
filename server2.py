import sys, Ice
from servants import FunctionsI

def run():
    with Ice.initialize(sys.argv) as communicator:

        adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -h 0.0.0.0 -p 5679")
        object1 = FunctionsI("Object1")
        object2 = FunctionsI("Object2")
        adapter.add(object1, Ice.stringToIdentity("SimpleFunctions1"))
        adapter.add(object2, Ice.stringToIdentity("SimpleFunctions2"))
        adapter.activate()
        print(f"Instanciado {object1.name} e {object2.name}, rodando na porta 5679...")
        communicator.waitForShutdown()
    
if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print(f"\nServidor (server2.py) encerrado por KeyboardInterrupt.")
        sys.exit(0)

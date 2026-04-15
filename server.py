import sys, Ice
from servants import FunctionsI
        
with Ice.initialize(sys.argv) as communicator:

    adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 5678")
    object = FunctionsI('objeto')
    adapter.add(object, Ice.stringToIdentity("SimpleFunctions"))

    adapter.activate()
    print("Servidor rodando na porta 5678...")
    communicator.waitForShutdown()
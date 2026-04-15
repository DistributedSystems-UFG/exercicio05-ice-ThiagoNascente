import sys, Ice

Ice.loadSlice(['-I.', 'Functions.ice'])
import Demo
 
class PrinterI(Demo.Printer):
    def __init__(self, t):
        super().__init__()
        self.t = t
        
    def printString(self, s, current=None):
        print(self.t, s)
        return f'Mensagem \'{s}\' escrita com sucesso'

with Ice.initialize(sys.argv) as communicator:

    adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
    object = PrinterI('Impressora disse: ')
    adapter.add(object, Ice.stringToIdentity("SimplePrinter"))
    adapter.activate()
    print("Servidor rodando na porta 11000...")
    communicator.waitForShutdown()
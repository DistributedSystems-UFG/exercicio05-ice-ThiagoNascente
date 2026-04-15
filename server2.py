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
    object1 = PrinterI("Object1 says:")
    object2 = PrinterI("Object2 says:")
    adapter.add(object1, Ice.stringToIdentity("SimplePrinter1"))
    adapter.add(object2, Ice.stringToIdentity("SimplePrinter2"))
    adapter.activate()

    communicator.waitForShutdown()

import sys, Ice

Ice.loadSlice(['-I.', 'Printer.ice'])
import Demo
 
with Ice.initialize(sys.argv) as communicator:

    base1 = communicator.stringToProxy("SimplePrinter1:tcp -h localhost -p 11000")
    base2 = communicator.stringToProxy("SimplePrinter2:tcp -h localhost -p 11000")
    printer1 = Demo.PrinterPrx.checkedCast(base1)
    printer2 = Demo.PrinterPrx.checkedCast(base2)
    if (not printer1) or (not printer2):
        raise RuntimeError("Invalid proxy")

    print(printer1.printString("Hello World from printer1!"))
    print(printer2.printString("Hello World from printer2!"))

    #communicator.waitForShutdown() #Isso acontece so em arquivos do tipo servidor

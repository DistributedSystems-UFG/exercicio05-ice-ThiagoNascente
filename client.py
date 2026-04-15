
import sys, Ice

Ice.loadSlice(['-I.', 'Functions.ice'])
import Demo

with Ice.initialize(sys.argv) as communicator:
    base = communicator.stringToProxy("SimplePrinter:default -p 11000")
    printer = Demo.PrinterPrx.checkedCast(base)
    if not printer:
        raise RuntimeError("Invalid proxy")

    print(printer.printString("Hello World! Comunicacao feita com sucesso!!!"))

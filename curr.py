print('Currency to be changed' + '\r\n' + '0:USD'+ '\r\n' + '1:EURO' + '\r\n' + '2:YEN' + '\r\n' + '3:YUAN' + '\r\n' + '4:AED' + '\r\n' + '5:SGD' + '\r\n' + '6:GBP' )

inr = float(input('What is the amount of INR you wish to convert?'))

def USD():
    return inr * 0.014

def EURO():
    return inr * 0.012

def YEN():
    return inr * 1.44

def YUAN():
    return inr * 0.091

def AED():
    return inr * 0.050

def SGD():
    return inr * 0.019

def GBP():
    return inr * 0.011

def convert_to(inr):
    switcher={
        0:USD,
        1:EURO,
        2:YEN,
        3:YUAN,
        4:AED,
        5:SGD,
        6:GBP
        }
    func = switcher.get(inr)
    print('The amount you converted is',func())
convert_to(4)
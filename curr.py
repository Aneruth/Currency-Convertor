inr = float(input('What is the amount of INR you wish to convert?'))
print('Please choose from this option \n\r' + '\n\r' + '0:USD' + '\n\r' + '1:EURO' + '\n\r' + '2:YEN' + '\n\r' + '3:YUAN' + '\n\r' + '4:AED' + '\n\r' + '5:SGD' + '\n\r' + '6:GBP' + '\n\r')

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
convert_to(type_curr)
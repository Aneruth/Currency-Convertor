inr = float(input('What is the amount of INR you wish to convert?'))
print('\n')
print('Please choose from this option \n\r' + '\n\r' + '0:USD' + '\n\r' + '1:EURO' + '\n\r' + '2:YEN' + '\n\r' + '3:YUAN' + '\n\r' + '4:AED' + '\n\r' + '5:SGD' + '\n\r' + '6:GBP' + '\n\r')
type_curr = int(input('Choose the currency mode:') + '\n')

def USD():
    return str(inr * 0.014) + ' USD'

def EURO():
    return str(inr * 0.012) + ' EURO'

def YEN():
    return str(inr * 1.44) + ' YEN'

def YUAN():
    return str(inr * 0.091) + ' YUAN'

def AED():
    return str(inr * 0.050) + ' AED'

def SGD():
    return str(inr * 0.019) + ' SGD'

def GBP():
    return str(inr * 0.011) + ' GBP'

def convert_to(type_curr):
    switcher={
        0:USD,
        1:EURO,
        2:YEN,
        3:YUAN,
        4:AED,
        5:SGD,
        6:GBP
        }
    # for i in switcher.items():
    #     if i == type_curr:
    #         i = switcher.get(type_curr)
    
    func = switcher.get(type_curr)
    print('\n')
    print('Amount you entered',str(inr) + ' INR')
    print('\n')
    print('You chose option {0}'.format(type_curr))
    print('\n')
    print('The amount you converted is',func())
convert_to(type_curr)
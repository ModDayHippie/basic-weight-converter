we = input('how much is the weight:')

wtype = input("kg or lbs:")

if wtype == 'lbs':
    weight = int(we) * 0.45
    print('so your the weight in Kg is: ')
    print(weight)
if wtype == 'kg':
    weight = int(we) * 2.204
    print('so the weight in LBS is:')
    print(weight)

input('Press Enter to Exit')
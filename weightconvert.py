we = input('how much is the weight')

wtype = input("kg or lbs")

if wtype == 'lbs':
    weight = int(we) * 0.45
    print('so your the weight is ')
    print(weight)
if wtype == 'kg':
    weight = int(we) * 2.204
    print('so the weight it')
    print(weight)
# calc a purchase value, with unit price of R$: 10,00
# Purchases of up to 10 units, without discount.
# Purchases between 11 and 20 units, 10% discount.
# Purchases above 10 units, 20% discount.

quantity = int(input('Type the quantity of units: '))
unitPrice = 10

if quantity <= 0:
    print('Invalid quantity')
elif quantity <= 10:
    print(f'Purchase value: R$ {quantity * unitPrice:.2f}')
elif quantity <= 20:
    print(f'Purchase value: R$ {quantity * (unitPrice * 0.9):.2f}')
else:
    print(f'Purchase value: R$ {quantity * (unitPrice * 0.8):.2f}')

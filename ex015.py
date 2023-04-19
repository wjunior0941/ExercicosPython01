km = float(input('Quantos KM rodado?'))
dias = int(input('Quantos dias? '))
pkm = km * 0.15
pdias = dias * 60
total = pkm + pdias
print('O preço a ser pago é de R${:.2f}'.format(total))
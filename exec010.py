real = float(input('quanto voce tem na carteira?R$ '))
dolar = real / 3.73
print("Com R${:.2f} você pode comprar US${:.2f}".format(real, dolar))
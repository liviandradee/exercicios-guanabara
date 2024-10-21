largura = float(input('Digite a largura da sua parede em metros:'))
altura = float(input('Digite a altura da sua parede em metros: '))
area = largura * altura
tinta = area / 2
print('Você precisa de {:.1f} litros de tinta para pintar sua casa'.format(tinta))
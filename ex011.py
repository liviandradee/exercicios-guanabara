preconormal = float(input('Digite o preço normal de um produto: R$'))
ValorDesconto = preconormal / 100 * 5
valorcomDesconto = preconormal - ValorDesconto
print ('O valor d produto com desconto de 5% é: {}.'.format(valorcomDesconto))
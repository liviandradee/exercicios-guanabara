KmPercorrido = float(input('Quantos kilometros você percorreu?: '))
QtdDias = int(input('Quantos dias você alugou?: '))

ValorTotal = (KmPercorrido * 0.15) + (QtdDias * 60)
print(f'O valor total a pagar por {QtdDias} dias e {KmPercorrido} kms é R${ValorTotal}')
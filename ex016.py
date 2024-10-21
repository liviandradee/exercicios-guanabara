import math

CatetoOposto = float(input('Digite o comprimento do cateto oposto: '))
CatetoAdjascente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusaOposto = math.exp2(CatetoOposto)
hipotenusaAdja = math.exp2(CatetoAdjascente)
hipotenusa = hipotenusaAdja + hipotenusaOposto
print(f'O valor da hipotenusa é de {hipotenusa}')


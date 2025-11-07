notas = [8.5, 4.0, 10.0, 7.5, 6.0, 9.0]
soma = 0
div = 0
notas_maiores_ou_iguais = 0
for num in notas:
    soma = soma + num
    div = div + 1
    media = soma / div
    if num >= 7.0:
        notas_maiores_ou_iguais += 1
print(media)
print(notas_maiores_ou_iguais)

lista_A = [1,2,3,4,5]
lista_B = [4,5,6,7,8]
comuns = []
for num_A in lista_A:
    if num_A in lista_B:
       comuns.append(num_A)
print(f"Os números que estão presentes em ambas as listas são: {comuns}")

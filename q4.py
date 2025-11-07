estoque = [
{"nome": "Teclado", "preco": 150.00, "quantidade": 5},
{"nome": "Mouse", "preco": 80.00, "quantidade": 12},
{"nome": "Monitor", "preco": 700.00, "quantidade": 3},
{"nome": "Headset", "preco": 250.00, "quantidade": 8}
]
print("-----Os produtos em menor quantidade são:------")
for num in estoque:
    if num["quantidade"] < 10:
       print(f". {num["nome"]}")

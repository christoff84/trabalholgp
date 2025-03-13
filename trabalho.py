# Exigência de Código 1 de 6 - Mensagem de boas-vindas
print("Bem-vindo ao sistema de vendas! Desenvolvido por Christoff Luz\n")

# Exigência de Código 2 de 6 - Entrada de dados
valor_unitario = float(input("Digite o valor unitário do produto: R$ "))
quantidade = int(input("Digite a quantidade desejada: "))

# Calculando o valor total sem desconto
valor_total_sem_desconto = valor_unitario * quantidade

# Exigência de Código 3 de 6 - Aplicação do desconto
if valor_total_sem_desconto < 2500:
    desconto = 0
elif 2500 <= valor_total_sem_desconto < 6000:
    desconto = 4
elif 6000 <= valor_total_sem_desconto < 10000:
    desconto = 7
else:
    desconto = 11

# Calculando o valor do desconto e o valor final com desconto
valor_desconto = (desconto / 100) * valor_total_sem_desconto
valor_total_com_desconto = valor_total_sem_desconto - valor_desconto

# Exigência de Código 4 de 6 - Exibição dos valores
print("\nResumo da compra:")
print(f"Valor total sem desconto: R$ {valor_total_sem_desconto:.2f}")
print(f"Desconto aplicado: {desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor total com desconto: R$ {valor_total_com_desconto:.2f}")

# Exigência de Código 5 de 6 - Uso de if, elif e else (já aplicado acima)

# Exigência de Código 6 de 6 - Comentários explicativos (inseridos ao longo do código)

# Exigência de Saída de Console 1 de 2 - Exibição da mensagem de boas-vindas (já implementada)

# Exigência de Saída de Console 2 de 2 - Garantir que há desconto se o valor for maior ou igual a 2500
if valor_total_sem_desconto >= 2500:
    print("\nParabéns! Você recebeu um desconto em sua compra.")
else:
    print("\nNenhum desconto aplicado. Para obter um desconto, compre acima de R$ 2500,00.")
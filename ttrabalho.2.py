# Exibindo mensagem de boas-vindas
print("Bem-vindo ao sistema de pedidos da loja! Desenvolvido por christoff luz")

# Dicionário com os preços dos produtos
precos = {
    "CP": {"P": 9, "M": 14, "G": 18},
    "AC": {"P": 11, "M": 16, "G": 20}
}

# Variável acumuladora para armazenar o valor total do pedido
total_pedido = 0

while True:
    # Solicitando o sabor ao usuário
    sabor = input("Digite o sabor (CP para Cupuaçu, AC para Açaí): ").upper()
    if sabor not in ["CP", "AC"]:
        print("Sabor inválido. Tente novamente")
        continue  # Retorna ao início do loop

    # Solicitando o tamanho ao usuário
    tamanho = input("Digite o tamanho (P, M, G): ").upper()
    if tamanho not in ["P", "M", "G"]:
        print("Tamanho inválido. Tente novamente")
        continue  # Retorna ao início do loop

    # Obtendo o preço do item selecionado
    preco = precos[sabor][tamanho]
    total_pedido += preco  # Acumulando o valor
    print(f"Pedido adicionado: {sabor} tamanho {tamanho} - R$ {preco}")

    # Perguntando se deseja continuar pedindo
    continuar = input("Deseja pedir mais alguma coisa? (S/N): ").upper()
    if continuar == "N":
        break  # Encerra o loop

# Exibindo o valor total do pedido
print(f"Total do pedido: R$ {total_pedido}")
print("Obrigado por comprar conosco!")
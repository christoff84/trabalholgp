# Exibindo mensagem de boas-vindas
print("Bem-vindo ao sistema de cobrança da copiadora! Desenvolvido por Christoff luz")

# Dicionário com os preços dos serviços
tabela_precos = {
    "DIG": 1.10,
    "ICO": 1.00,
    "IPB": 0.40,
    "FOT": 0.20
}

def escolha_servico():
    """Pergunta o serviço desejado e retorna o valor do serviço escolhido."""
    while True:
        servico = input("Escolha o serviço (DIG/ICO/IPB/FOT): ").upper()
        if servico in tabela_precos:
            return tabela_precos[servico]
        print("Serviço inválido. Tente novamente.")

def num_pagina():
    """Pergunta o número de páginas e aplica os descontos conforme a tabela do enunciado."""
    while True:
        try:
            paginas = int(input("Digite o número de páginas: "))
            if paginas >= 20000:
                print("Quantidade de páginas não permitida. Tente novamente.")
                continue
            elif paginas >= 2000:
                return paginas * 0.75  # 25% de desconto
            elif paginas >= 200:
                return paginas * 0.80  # 20% de desconto
            elif paginas >= 20:
                return paginas * 0.85  # 15% de desconto
            else:
                return paginas  # Sem desconto
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")

def servico_extra():
    """Pergunta sobre o serviço adicional e retorna o valor extra correspondente."""
    extras = {"1": 15, "2": 40, "0": 0}
    while True:
        opcao = input("Deseja encadernação? (1 - Simples, 2 - Capa Dura, 0 - Nenhum): ")
        if opcao in extras:
            return extras[opcao]
        print("Opção inválida. Tente novamente.")

# Execução do programa principal
preco_servico = escolha_servico()
n_paginas = num_pagina()
adicional = servico_extra()

total = (preco_servico * n_paginas) + adicional
print(f"Total a pagar: R$ {total:.2f}")
print("Obrigado por utilizar nossos serviços!")
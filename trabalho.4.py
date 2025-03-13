# Mensagem de boas-vindas
print("Bem-vindo ao sistema de gerenciamento de livros! Desenvolvido por Christoff Luz")

# Lista para armazenar os livros
lista_livros = []
# ID global para controle dos livros cadastrados
id_global = 0


def cadastrar_livro(id):
    """Cadastra um novo livro na lista_livros."""
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite o nome da editora: ")

    livro = {"ID": id, "Nome": nome, "Autor": autor, "Editora": editora}
    lista_livros.append(livro)
    print(f"Livro '{nome}' cadastrado com sucesso!\n")


def consultar_livro():
    """Consulta os livros cadastrados com diferentes opções."""
    while True:
        print("\nConsultar Livro:")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Autor")
        print("4. Retornar ao menu")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nLista de Todos os Livros:")
            for livro in lista_livros:
                print(livro)
        elif opcao == "2":
            id_busca = int(input("Digite o ID do livro: "))
            livro_encontrado = next((livro for livro in lista_livros if livro["ID"] == id_busca), None)
            print(livro_encontrado if livro_encontrado else "ID não encontrado.")
        elif opcao == "3":
            autor_busca = input("Digite o nome do autor: ")
            livros_encontrados = [livro for livro in lista_livros if livro["Autor"].lower() == autor_busca.lower()]
            if livros_encontrados:
                for livro in livros_encontrados:
                    print(livro)
            else:
                print("Nenhum livro encontrado para esse autor.")
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")


def remover_livro():
    """Remove um livro da lista_livros pelo ID."""
    while True:
        try:
            id_remover = int(input("Digite o ID do livro a ser removido: "))
            for livro in lista_livros:
                if livro["ID"] == id_remover:
                    lista_livros.remove(livro)
                    print("Livro removido com sucesso!\n")
                    return
            print("ID inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")


# Menu principal
while True:
    print("\nMenu:")
    print("1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Remover Livro")
    print("4. Encerrar Programa")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == "2":
        consultar_livro()
    elif opcao == "3":
        remover_livro()
    elif opcao == "4":
        print("Programa encerrado. Obrigado!")
        break
    else:
        print("Opção inválida. Tente novamente.")

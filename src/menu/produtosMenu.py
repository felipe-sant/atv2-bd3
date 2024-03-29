from menu.produtos.produtosCreateMenu import produtosCreateMenu
from menu.produtos.produtosReadMenu import produtosReadMenu
from menu.produtos.produtosUpdateMenu import produtosUpdateMenu
from menu.produtos.produtosDeleteMenu import produtosDeleteMenu

def produtosMenu():
    execucao = True

    while execucao:
        print("-=-"*20)
        print("Produtos")
        print("1 - Criar Produto")
        print("2 - Ler Produto")
        print("3 - Atualizar Produto")
        print("4 - Deletar Produto")
        print("0 - Voltar")
        print("-=-"*20)

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            produtosCreateMenu()
        elif opcao == "2":
            produtosReadMenu()
        elif opcao == "3":
            produtosUpdateMenu()
        elif opcao == "4":
            produtosDeleteMenu()
        elif opcao == "0":
            execucao = False
        else:
            print("Opção inválida!")
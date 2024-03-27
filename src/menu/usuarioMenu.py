from menu.usuario.usuarioCreateMenu import usuarioCreateMenu
from menu.usuario.usuarioReadMenu import usuarioReadMenu
from menu.usuario.usuarioUpdateMenu import usuarioUpdateMenu
from menu.usuario.usuarioDeleteMenu import usuarioDeleteMenu

def usuarioMenu():
    execucao = True

    while execucao:
        print("-=-"*20)
        print("Usuários")
        print("1 - Criar Usuário")
        print("2 - Ler Usuário")
        print("3 - Atualizar Usuário")
        print("4 - Deletar Usuário")
        print("0 - Voltar")
        print("-=-"*20)

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            usuarioCreateMenu()
        elif opcao == "2":
            usuarioReadMenu()
        elif opcao == "3":
            usuarioUpdateMenu()
        elif opcao == "4":
            usuarioDeleteMenu()
        elif opcao == "0":
            execucao = False
        else:
            print("Opção inválida!")
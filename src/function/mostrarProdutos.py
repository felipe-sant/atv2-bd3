def mostrarProdutos(produtos):
    print("Produtos:")
    for produto in produtos:
        print("     "+"ID:", produto["_id"])
        print("     "+"Nome:", produto["nome"])
        print("     "+"Descrição:", produto["descricao"])
        print("     "+"Preço:", produto["preco"])
        print()
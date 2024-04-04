from database.connection import database
from bson.objectid import ObjectId

def produtoUpdate(filtro):
    global database
    produto = database.produto.find_one(filtro)

    print()
    if produto == None:
        print("Produto não encontrado")
        return
    
    print()
    print(f"- Você esta alterando o produto {produto["nome"]} -")
    print("Deixe em branco para manter o mesmo valor")
    print()

    nome = input("Digite o novo nome: ")
    if nome == "":
        nome = produto["nome"]
    
    vendedorID = str(input("Digite o id do novo vendedor: "))
    if vendedorID == "":
        id = produto["vendedor"]["_id"]
        vendedorNome = produto["vendedor"]["nome"]
    else:
        id = ObjectId(vendedorID)
        vendedor = database.vendedor.find_one({"_id": id})
        if vendedor == None:
            print()
            print("Vendedor não encontrado!")
            input()
            return
        else:
            vendedorNome = vendedor["nome"]


    descricao = input("Digite a nova descrição: ")
    if descricao == "":
        descricao = produto["descricao"]

    try:
        preco = float(input("Digite o novo preço: "))
    except:
        preco = produto["preco"]

    try:
        estoque = int(input("Digite o novo estoque: "))
    except:
        estoque = produto["estoque"]

    novoProduto = {
        "nome": nome.lower(),
        "vendedor": {
            "_id": id,
            "nome": vendedorNome
        },
        "descricao": descricao.lower(),
        "preco": preco,
        "estoque": estoque,
    }

    database.produto.update_one(filtro, { "$set": novoProduto })
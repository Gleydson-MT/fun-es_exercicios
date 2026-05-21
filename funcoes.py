# Q1
def cabecalho(titulo):
    print("-"*40)
    print(f"{titulo.center(40)}")
    print("-"*40)
# Q2
def tabuada(numero):
    for i in range(1,11):
        resultado = numero * i
        print(f"{numero} - {i:2d} = {resultado:2d}")
# Q3
def calcular_imc(nome, peso, altura):
    imc = peso / (altura**2)
    print(f"{nome}: IMC = {imc:.2f}")
# Q4
def exibir_produto(nome, preco, quantidade):
    subtotal = preco * quantidade
    print(f"""
Produto: {nome} 
Preço: {preco} 
Qtd: {quantidade}
print()
Subtotal: {subtotal:.2f}
 """)
# Q5
def aplicar_desconto(preco, desconto=10):
    valor_desconto = preco * desconto / 100
    print(f""""
Preço original: R$ {preco}
Desconto {desconto}: R$ {valor_desconto}
Preço final: R$ {preco-valor_desconto}          
 """)
# Q6
def registrar_pedido(sabor, tamanho=("Média"), borda=("Simples")):
    print(f""" 
Sabor: {sabor}
Tamanho: {tamanho}
Borda: {borda}
 """)

registrar_pedido("Calabresa")
registrar_pedido("Frango", "Grande")
registrar_pedido("Portugesa", "Familia", "Catupiry")
registrar_pedido("Margherita", borda="Cheddar")
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
# Q7
def calcular_troco(total, pago):
    if pago < total:
        troco = 0
        print("Erro: valor pago insuficiente.")
        return troco
    else:
        troco = pago - total
        return troco
# Q8
def calcular_media(n1, n2, n3, n4):
    media = (n1 + n2 + n3 + n4) / 4
    return media

media1 = calcular_media(8.0, 7.5, 9.0, 8.5)
if media1 >= 7:
    situacao1 = "Aprovado"
elif media1 >= 5:
    situacao1 = "Recuperação"
else:
    situacao1 = "Reprovado"
print(f"Lucas | Média: {media1:.2f} | {situacao1}")

media2 = calcular_media(5.0, 4.0, 2.5, 3.5)
if media2 >= 7:
    situacao2 = "Aprovado"
elif media2 >= 5:
    situacao2 = "Recuperação"
else:
    situacao2 = "Reprovado"
print(f"Marina | Média: {media1:.2f} | {situacao1}")

media3 = calcular_media(3.0, 4.0, 2.5, 3.5)
if media3 >= 7:
    situacao3 = "Aprovado"
elif media2 >= 5:
    situacao3 = "Recuperação"
else:
    situacao3 = "Reprovado"
print(f"Pedro | Média: {media1:.2f} | {situacao1}")

# Q9
# Leia o código abaixo com atenção e responda as três perguntas **sem executar o programa**. O objetivo é entender o que acontece com variáveis de mesmo nome em escopos diferentes.

# ```python
# x = 10

# def dobrar():
#     x = 20
#     print(x)

# dobrar()
# print(x)
# ```
# a) Escreva exatamente o que será impresso no terminal, linha por linha. Justifique cada linha com base no conceito de escopo.
# R: Linha 1.: x = 10, por está fora da função se torno global
# linha 2.: def dobrar():
#             x = 20
#             print(x)
# Aqui como o "x" está dentro da função então ele equivale a "20", pois não foi expecificado que fosse ultilizado o "x global", então quando der o print, será retornado o valor de "40"
# linha 3.: dobrar()
#           print(x)
# Aqui esta sendo chamada a função "dobrar()", então será impresso o número 40, logo a baixo ao dar print(x), será exibido o 10, pois está se referindo ao "x global".

# b) A linha `x = 20` dentro de `dobrar()` altera o valor do `x` que está fora da função? Explique por quê.
# R: Não, pois o "x" dentro da função pertece a ela mas o "x" de fora se refere ao "x global", ou seja será usado por padrão caso não seja expecificado que se ultilize dentro da função, ele não sofrerá alteração.

# c) Reescreva a função `dobrar` de forma correta: ela deve receber um número por parâmetro, calcular o dobro e **retornar** o resultado. Fora da função, chame-a com `x = 10` e exiba o resultado com `print`.

def dobrar(n):
    x = n * 2
    return  x

x = 10

print(f"O dobro de {"global"} é {x}")
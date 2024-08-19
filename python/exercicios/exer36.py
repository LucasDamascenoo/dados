

# %%
# # Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

# %%
valor_casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual é o seu sálario: "))
anos_financiamento = int(input("Quantos anos deseja pagar? "))
prestacao = valor_casa / (anos_financiamento*12)

limite_prestacao = salario * 0.30

if prestacao > limite_prestacao:
    print(f"o valor da prestação R${
          prestacao} ultrapa o limite da prestação R${limite_prestacao}")
else:
    print(f"Parábens, você pode comprar o imovel: o valor da prestação será R${
          prestacao:.2f}")

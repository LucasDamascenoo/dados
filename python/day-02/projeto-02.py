# tip calculator

mensagem = input("Welcome to the tip calculator!!! ")

valor_da_conta = float(input("Qual o total da conta? "))
gorjeta = int(input("Quanto de gorjeta gostaria de dar? 10,12 ou 15? "))
total_de_pessoas = int(input("Quantas pessoas vão dividir a conta? "))

total_conta = valor_da_conta + gorjeta
total_por_pessoa =  total_conta / total_de_pessoas

print(f"O valor da conta deu R${valor_da_conta} + R${gorjeta} = R${total_conta}, dividimos por {total_de_pessoas} pessoas e o total por pessoa foi de R${total_por_pessoa}")
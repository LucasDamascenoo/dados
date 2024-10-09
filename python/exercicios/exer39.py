
# dado o ano de nascimento, vejo se já tem 18, caso contrario quantos anos faltam pro alistamento militar

# dado o ano de nascimento, vejo se já tem 18, caso contrario quantos anos faltam pro alistamento militar

from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nascimento

if (idade == 18):
    print(f'voce precisa se alistar emediatamente')
elif (idade < 18):
    print(f'ainda faltam {ano_atual - ano_nascimento} anos pro alistamento')
else:
    print(f'voce deveria ter se alistado a {ano_atual - idade} anos')

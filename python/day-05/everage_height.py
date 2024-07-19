
student_height = [156, 178, 165, 171, 187]


soma_altura = 0

for soma in student_height:
    soma_altura += soma
print(f"a soma de altura é =  {soma_altura}")


qtd_alunos = 0


for qtd in student_height:
    qtd_alunos += 1
print(f"a qtd de alunos é: {qtd_alunos} alunos")


media = round(soma_altura/qtd_alunos)
print(f"média_das_alturas: {media}")

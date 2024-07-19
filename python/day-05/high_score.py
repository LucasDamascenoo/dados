# dado uma lista, traga o maior numero dela (sem usar min e max)


student_score = [78, 65, 89, 86, 55, 91, 64, 89]

maior_nota = 0
for score in student_score:
    if score > maior_nota:
        maior_nota = score


print(f"A maior nota é: {maior_nota}")

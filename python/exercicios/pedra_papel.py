
import random
# programa consiste em um jogo de pedra papel e tesoura
# uma entrada do user 0 para pedra 1 para papel
# a escolha do computador eh aleatoria
# verificar qm ganhou, caso seja 1 > 2 ganha, else perde


rock = """

      _______
----'   ____)
      (_____)
      (_____)
      (____)
----.__(___)


"""

paper = """

     _______
----'   ____)____
          ______)
          _______)
         _______)
----.__________)

"""


scissors = """

     _______
----'   ____)____
          ______)
       __________)
      (____)
----.__(___)


"""
image = [rock, paper, scissors]


user_choice = int(
    input('Escolha 0 para pedra, e 1 para papel e 2 para tesoura: '))
print(image[user_choice])

computer_choice = random.randint(0, 2)
print(image[computer_choice])


if user_choice >= 3 and user_choice < 0:
    print('escolha errada: voce perdeu')
elif user_choice == 0 and computer_choice == 2:
    print("Você ganhou!")
elif user_choice == 1 and computer_choice == 0:
    print("Você ganhou!")
elif user_choice == 2 and computer_choice == 1:
    print("Você ganhou!")
elif user_choice == computer_choice:
    print('empate')

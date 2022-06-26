import random
num = random.randint(1, 100)
print("відгадай задане ціле число від 1 до 100 включно")
print("введіть ваше число ")
num_user = int(input(": "))

if num_user < 0:
    print("число не входить в заданий діапазон!!!")
    print("спробуйте ввести число з заданого діапазону")
    num_user = int(input(": "))
elif num_user > 100:
    print("число не входить в заданий діапазон!!!")
    print("спробуйте ввести число з заданого діапазону")
    num_user = int(input(": "))
else:
    print()

col = 0
while num_user != num:
    col += 1
    if num_user < num:
        print("ваше число замале...")
    else:
        print("ваше число завелике...")
    num_user = int(input("спробуйте відгадати ще раз: "))
print("ТАК, ви вгадали!!!")

print("ви відгадали число з:", col, "спроб")

print("задане число було ", num)

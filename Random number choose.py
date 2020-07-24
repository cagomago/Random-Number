import random

sayi = random.randint(1 , 99)
tahmin = 0
say = 0

while tahmin != sayi and tahmin != "exit":
    tahmin = input("tahmin et?")

    if tahmin == "exit":
        break

    guess = int(tahmin)
    say += 1

    if guess < sayi:
        print("cok dusuk!")
    elif guess > sayi:
        print("cok yuksek!")
    else:
        print("harika!")
        print(":)" , say , ":))")
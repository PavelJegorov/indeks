print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Sisesta oma nimi: ")
print(nimi, " oi kui ilus nimi")
print (nimi, "! Kas leian Sinu keha indeksi? 0-ei, 1-jah =>")
if vastus ==1:
    pikkus = int(input("Введите cвой рост в (см)")) #данные для массы тела
    mass = float(input("Введите свой вес в (kg)"))
    indeks = mass /(0.01 * pikkus) ** 2
    print(nimi, "! Sinu keha indeks on:" )


if indeks<16:
    print("Tervisele ohtlik alakaal")
elif 16<= indeks<19:
    print("Alakaal")
elif 19<= indeks<25:
    print("Normaalkaal")
elif 25<= indeks<30:
    print("Ülekaal")
elif 30<= indeks<35:
    print("Rasvumine")
elif 35<= indeks<40:
    print("Tugev rasvumine")
elif >40:
    print("Tervisele ohtlik rasvumine")


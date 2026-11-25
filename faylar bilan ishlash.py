#1-misol
with open("matn.txt", "r") as file:
    matn = file.read()
sozlar = matn.split()
with open("natija.txt", "w") as file:
    for soz in sozlar:
        if len(soz) > 5:
            file.write(soz + "\n")
print("Natija natija.txt fayliga yozildi!")
#2-misol
talabalar = []
with open("talabalar.txt", "r") as fayl:
    for qator in fayl:
        ism, ball = qator.split()
        ball = int(ball)
        talabalar.append((ism, ball))
with open("yuqori.txt", "w") as y:
    with open("past.txt", "w") as p:
        for ism, ball in talabalar:
            if ball >= 80:
                y.write(f"{ism} {ball}\n")
            else:
                p.write(f"{ism} {ball}\n")
eng_yuqori = max(talabalar, key=lambda talaba: talaba[1])
print("Eng yuqori ball olgan talaba:")
print(eng_yuqori[0], eng_yuqori[1])

#3-misol
takrorlangan = []
natija = []
with open("matn.txt", "r") as f:
    for soz in f:
        soz = soz.strip()
        takrorlangan.append(soz)
for soz in takrorlangan:
    print(soz)
with open("takrorlar.txt", "w") as f:
    for soz in takrorlangan:
        if takrorlangan.count(soz) > 1 and soz not in natija:
            natija.append(soz)
            f.write(soz + "\n")
print(natija)
#4-misol
kitob = input("Kitob nomini kiriting: ")
topildi = False
with open("kitoblar.txt", "r") as f:
    for qator, nom in enumerate(f, start=1):
        nom = nom.strip()
        if nom == kitob:
            print("Kitob topildi!")
            print("Qator raqami:", qator)
            topildi = True
            break
if topildi == False:
    print("Kitob topilmadi")
#5-misol
with open("matn.txt", "r") as f:
    matn = f.read()
matn = matn.upper()
matn = matn.replace("PYTHON", "DASTURLASH")
with open("yangi_matn.txt", "w") as f:
    f.write(matn)
print("Matn o'zgartirildi!")

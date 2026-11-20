class Avto:
    def __init__(self, model, rang, koropka, narx):
        self.model = model
        self.rang = rang
        self.koropka = koropka
        self.narx = narx
        self.kilometr = 30000

    def get_info(self):
        return f"Modeli: {self.model},rangi {self.rang},koropkasi {self.koropka},narxi {self.narx}"

    def narxi(self):
        return f"{self.narx}"

    def set_kilometr(self,kilometr):
        self.kilometr = kilometr

    def update_km(self):
        self.kilometr += 1

    def modeli(self):
        return self.model
avto = Avto("Santa fe","oq","ovtomat","740 million so'm",)
avto.kilometr = 32000
print(avto.kilometr)
print(avto.get_info())


class Avtosalon:
    def __init__(self,salon_nomi,manzili,sotuvdagi_avto):
        self.salon_nomi = salon_nomi
        self.manzili = manzili
        self.sotuvdagi_avto = sotuvdagi_avto
        self.sotuv_avto = []
    def manzil(self):
        return self.manzili

    def s_avtomobil(self):
        return self.sotuvdagi_avto

    def s_nomi(self):
        return self.salon_nomi

    def add_avto(self):
        self.sotuv_avto.append(self)

salon = Avtosalon("Zumrad","Xorazm","cobalt")
print(salon.s_avtomobil())
print(salon.s_nomi())

print(dir(Avto))
print(avto.__dict__)
print(dir(Avtosalon))
print(dir(salon))

print(dir(str))
print(dir(list))
print(dir(int))
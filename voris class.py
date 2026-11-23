
# class Fan:
#     def __init__(self, nomi):
#         self.nomi = nomi
#
# class Talaba:
#     def __init__(self, ism, familiya, yosh):
#         self.ism = ism
#         self.familiya = familiya
#         self.yosh = yosh
#         self.fanlar = []
#
#     def fanga_yozil(self, *fanlar):
#         for fan in fanlar:
#             self.fanlar.append(fan)
#
#     def remove_fan(self, fan):
#         if fan in self.fanlar:
#             self.fanlar.remove(fan)
#         else:
#             print("Siz bu fanga yozilmagansiz")
#
#     def get_info(self):
#         print(f"Talaba: {self.ism} {self.familiya}")
#         print("Fanlar:")
#         for fan in self.fanlar:
#             print(f"- {fan.nomi}")
#
# class Shaxs:
#     def __init__(self, ism, familiya, yosh):
#         self.ism = ism
#         self.familiya = familiya
#         self.yosh = yosh
#
#     def get_info(self):
#         return f"{self.ism} {self.familiya}, {self.yosh} yosh"
#
# class Professor(Shaxs):
#     def __init__(self, ism, familiya, yosh, fan):
#         super().__init__(ism, familiya, yosh)
#         self.fan = fan
#
#     def get_info(self):
#         return f"Professor: {self.ism} {self.familiya}, Fan: {self.fan}"
#
# class Foydalanuvchi(Shaxs):
#     def __init__(self, ism, familiya, yosh, username):
#         super().__init__(ism, familiya, yosh)
#         self.username = username
#
#     def get_info(self):
#         return f"Foydalanuvchi: {self.username}, {self.ism} {self.familiya}"
#
# class Sotuvchi(Shaxs):
#     def __init__(self, ism, familiya, yosh, mahsulot):
#         super().__init__(ism, familiya, yosh)
#         self.mahsulot = mahsulot
#
#     def get_info(self):
#         return f"Sotuvchi: {self.ism}, Mahsulot: {self.mahsulot}"
#
# class Mijoz(Shaxs):
#     def __init__(self, ism, familiya, yosh, balans):
#         super().__init__(ism, familiya, yosh)
#         self.balans = balans
#
#     def get_info(self):
#         return f"Mijoz: {self.ism}, Balans: {self.balans}"

# class Admin(Foydalanuvchi):
#     def __init__(self, ism, familiya, yosh, username):
#         super().__init__(ism, familiya, yosh, username)
#
#     def ban_user(self):
#         print("Foydalanuvchi bloklandi")
#
#     def get_info(self):
#         return f"Admin: {self.username}, {self.ism} {self.familiya}"
#
# matematika = Fan("Matematika")
# fizika = Fan("Fizika")
# python = Fan("Python")
#
# talaba = Talaba("Ali", "Valiyev", 20)
#
# talaba.fanga_yozil(matematika, fizika, python)
# talaba.get_info()
#
# talaba.remove_fan(fizika)
# talaba.get_info()
#
# professor = Professor("Anvar", "Aliyev", 45, "Matematika")
# foydalanuvchi = Foydalanuvchi("Vali", "Valiyev", 25, "vali123")
# sotuvchi = Sotuvchi("Hasan", "Karimov", 30, "Telefon")
# mijoz = Mijoz("Husan", "Aliyev", 28, 500000)
# admin = Admin("Akmal", "Valiyev", 35, "admin01")
#
# print(professor.get_info())
# print(foydalanuvchi.get_info())
# print(sotuvchi.get_info())
# print(mijoz.get_info())
# print(admin.get_info())
# admin.ban_user()






#2-misol

# Shaxs klassi
# class Shaxs:
#     odamlar_soni = 0
#
#     def __init__(self, ism, familiya, yosh, passport):
#         self.ism = ism
#         self.familiya = familiya
#         self.yosh = yosh
#         self.__passport = passport
#         Shaxs.odamlar_soni += 1
#     def get_passport(self):
#         return self.__passport
#     def set_passport(self, yangi_passport):
#         self.__passport = yangi_passport
#
#     def get_info(self):
#         return f"{self.ism} {self.familiya}, {self.yosh} yosh"
#     @classmethod
#     def get_odamlar_soni(cls):
#         return cls.odamlar_soni

# class Talaba(Shaxs):
#     talabalar_soni = 0
#     def __init__(self, ism, familiya, yosh, passport, student_id):
#         super().__init__(ism, familiya, yosh, passport)
#         self.student_id = student_id
#         self.__manzil = "Noma'lum"
#         self.fanlar = []
#         Talaba.talabalar_soni += 1
#     def get_manzil(self):
#         return self.__manzil
#     def set_manzil(self, yangi_manzil):
#         self.__manzil = yangi_manzil
#     @classmethod
#     def get_talabalar_soni(cls):
#         return cls.talabalar_soni
#     def get_info(self):
#         return f"Talaba: {self.ism} {self.familiya}, ID: {self.student_id}"
# shaxs1 = Shaxs("Ali", "Valiyev", 40, "AA1234567")
# talaba1 = Talaba("Vali", "Aliyev", 20, "AB7654321", "T001")
# talaba2 = Talaba("Hasan", "Karimov", 21, "AC1234567", "T002")
#
# print(shaxs1.get_info())
# print("Passport:", shaxs1.get_passport())
# shaxs1.set_passport("AA9999999")
# print("Yangi passport:", shaxs1.get_passport())
# print(talaba1.get_info())
# print("Manzil:", talaba1.get_manzil())
# talaba1.set_manzil("Toshkent shahri")
# print("Yangi manzil:", talaba1.get_manzil())
# print("Odamlar soni:", Shaxs.get_odamlar_soni())
# print("Talabalar soni:", Talaba.get_talabalar_soni())



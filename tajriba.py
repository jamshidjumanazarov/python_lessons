class user:
    def __init__(self, ism, familiya , email , t_yil , t_oy , t_kun):
        self.ism = ism
        self.familiya = familiya
        self.email = email
        self.t_yil = t_yil
        self.t_oy = t_oy
        self.t_kun = t_kun
    def get_ism(self):
        return self.ism
    def get_famuliya(self):
        return self.familiya
    def get_tism(self):
        return f"{self.familiya} {self.ism}"
    def get_pochta(self):
        return self.email
    def get_tsana(self):
        return f"{self.t_kun}.{self.t_oy}.{self.t_yil}"
    def get_info(self):
        return f"Foydalanuvchi: {self.familiya} {self.ism}, tug'ilgan sanasa: {self.t_yil}.{self.t_oy}.{self.t_kun}, emayili: {self.email}"
user_1 = user("Jamshidbek","Jumanazarov","jumanazarovjamshid777@.gmail.com",2007,3,31)
name = user("Jamshidbek","Jumanazarov","jamshidbek@gmail.com",2007,3,31)
print(user_1.get_info())
print(name.get_tism())
print(user_1.get_pochta())

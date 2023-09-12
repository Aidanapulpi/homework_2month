class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return self.name

    def double_health_points(self):
        self.health_points *= 2

    def __str__(self):
        return (f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health Points: {self.health_points}")

    def __len__(self):
        return len(self.catchphrase.replace(" ", ""))


hero = SuperHero("Iron Man", "Shellhead", "Powered Armor", 100, "I am Iron Man")
print(hero.get_name())
hero.double_health_points()
print(hero)
len_phrase = len(hero)
print(f"Len catchphrase: {len_phrase}")


class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def double_health_points(self):
        self.health_points **= 2
        self.fly = True

    def true_phrase(self):
        return f"True in the True_phrase"


class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def double_health_points(self):
        self.health_points **= 2
        self.fly = True

    def true_phrase(self):
        return f"True in the True_phrase"


print()
hero2 = AirHero("Superman", "flyman07", "fly",
                30, "I can kill you", 34)
print(hero2.get_name())
hero2.double_health_points()
print(hero2, f',fly in:{hero2.true_phrase()}')
print()
hero3 = EarthHero("Hulkman", "stoneman", "beat", 40,
                  "I am a big man", 45)
print(hero3.get_name())
hero3.double_health_points()
print(hero3, f',fly in:{hero3.true_phrase()}')


class Villian(EarthHero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self, hero2):
        hero2.damage **= 2
        return hero2.damage


monster1 = Villian("spirit" , "spirit05", "can run", 38 ,
                   "i can run" , 26)
print()
print(monster1.get_name())
print(monster1)
print()
print(f'hero Superman damage: {monster1.crit(hero2)}')

class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_hero_name(self):
        print("Hero Name:", self.name)

    def double_health_points(self):
        self.health_points *= 2

    def magic_info(self):
        print("Nickname:", self.nickname)
        print("Superpower:", self.superpower)
        print("Health Points:", self.health_points)

    def magic_phrase_length(self):
        return len(self.catchphrase)


hero = SuperHero(
    name="Superman",
    nickname="Man of Steel",
    superpower="Flight, Super strength, Heat Vision",
    health_points=100,
    catchphrase="Up, up and away!"
)

hero.get_hero_name()
hero.double_health_points()
hero.magic_info()
phrase_length = hero.magic_phrase_length()
print("Catchphrase Length:", phrase_length)
class Character:
    def __init__(self, health, speed, damage):
        self.health = health
        self.speed = speed
        self.damage = damage
    def double_speed(self):
        self.speed = self.speed * 2
bruh = Character(10, 20, 2)
monkey = Character(8, 35, 4)

monkey.double_speed()
print(monkey.speed)
monkey.double_speed()
print(monkey.speed)


from chef import Chef


class ChineseChef(Chef):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def can_make_chinese_dish(self):
        print(self.name + ', who is a ' + self.type + ' chef makes good chinese food')

    def can_make_food(self): #method override
        print(self.name + ' Makes excellent food!')

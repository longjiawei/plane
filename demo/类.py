class Fruit:
    color = "绿色"
    def harvest(self,color,name):
        print(name+"是"+ color +"的!")
class Apple(Fruit):
    color = "红色的"
    def __init__(self):
        print("我是苹果")
class Orange(Fruit):
    color = "橙色"
    def __init__(self):
        print("我是橘子")
apple = Apple()
apple.harvest(apple.color,"苹果")
orange = Orange()
orange.harvest(orange.color,"橘子")

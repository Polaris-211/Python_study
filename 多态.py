class Animal:
    def speak(self): #抽象类：方法体空实现，由子类决定，提供设计标准
        pass
class Dog(Animal):
    def speak(self):
        print("wangwangwang")
class Cat(Animal):
    def speak(self):
        print("miaomiaomiao")

def make_noise(animal: Animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)
class Animal:
    def __init__(self,name):
        self.name= name
    def display(self):
        print(f"About {self.name}: ")
        

class animal(Animal):
    def __init__(self,name,lifespan,sound):
        Animal.__init__(self,name)   
        self.sound=sound
        self.lifespan=lifespan

    def attribute(self):
        my_attribute = Animal.display(self)

        return f"{self.name} is a mammal.\nIt's lifespan is {self.lifespan} years.\nIt makes a {self.sound} sound"   
        
anim1=animal("Cat","12 to 14" ,"MeowMeow")
anim2=animal("Dog",15,"BhawBhaw")
anim3=animal("Lion",18,"roar")

print(anim1.attribute())
print("\n")
print(anim2.attribute())
print("\n")
print(anim3.attribute())
print("\n")




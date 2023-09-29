class Vehicle:
    def __init__(self,name,year):
        self.name=name
        self.year=year
    def display_info(self):
        print(f"Name: {self.name}")
        # print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        # print(self.name, self.model,self.year)
        
class Car(Vehicle):
    def __init__(self,name,model,year):
       Vehicle.__init__(self,name,year)
       self.model=model
       
       
    def display_info(self):
        Vehicle.display_info(self)
        print(f"model: {self.model}")
        return f"{Vehicle}, Year: {self.model}"
        
myCar=Car("toyota", "carmy", 2022)

myCar.display_info()
        
      
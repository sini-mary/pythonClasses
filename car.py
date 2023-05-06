class Car:
    make="Benz"
    
    def __init__(self,model,age,color) :
        self.model:model
        self.age=age
        self.color=color
        
    def start_engine(self):
        return f"{self.make}{self.model} engine works"
    
    def mileAge(self):
        return f"the mileAge of {self.make} is zero"

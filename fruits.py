class Fruits:
     name="fruits"
     def __init__(self,berries,citrus,melons):
         self.berries=berries
         self.citrus=citrus
         self.melons=melons
         
     def taste(self):
         return f"{self.citrus} tastes bitter "
     
     def skin(self):
         return f"{self.berries} have thin outer skin while {self.citrus} have thin outer rind"
     
    
          
class User:
    name = ""
    age = ""
    health= ""
    def __init__(self,name, age, health):
        self.name = name
        self.age = age
        self.health = health
    
    def is_eligible(self):
        if self.age >= 18 and self.age <= 60 and self.health >= 5:
            return True
        return False
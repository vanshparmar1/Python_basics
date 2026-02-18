class tealeafage:
    def __init__(self,age):
        self.age = age
    
    #method to get value out of the class
    @property
    def age(self):
        return self._age+2
    
    #responsible for how you set the value inside the class
    @age.setter
    def age(self,age):
        if age<5:
            self._age = age
        else:
            raise ValueError(
                "tea leaf age must be under 1-5 years"
            )
leaf = tealeafage(2)
print(leaf.age)

        
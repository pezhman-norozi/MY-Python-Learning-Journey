class Animal :
    Zoo_name = "Zebra"
    def __init__(self , name , species , age , sound):
        self.name = name 
        self.species = species
        self.age = age
        self.sound = sound
        
    def make_sound(self) :
        print(f"{self.name} says {self.sound}")
        
    def info(self) :
        print(f"Name : {self.name} species : {self.species} age : {self.age} Zoo : {Animal.Zoo_name} ")   
    
    def __str__(self):
        return f"{self.name} , {self.species} , {self.age} , {self.sound}"
            

class Bird(Animal) :
    def __init__(self, name, species, age, sound , wing_span):
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span
        
    def make_sound(self) :
        print(f"{self.name} chirps {self.sound}")

        
lion = Animal ("ziba" , "Darande" , 22 , "OOOOOOH")
parrot = Bird ("bilmaz" , "naz" , 10 , "Jic_Jic" , 5.4 )

lion.make_sound()
lion.info()  

parrot.make_sound()
parrot.info()
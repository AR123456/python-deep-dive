class Animal:
    def __init__(self):
    #defining attributes
        self.num_eyes = 2
    # defining method associated with the animal class
    def breathe(self):
        print("Inhale, exhale.")
# passing Animal into Fish class so Fish has all the attributes
# and methonds from the Animal class, then can have some of its own
class Fish(Animal):
    def __init__(self):
        # making call to super class which in this case is Animal
        # and init it
        super().__init__()

    def breathe(self):
        #bring in super class and call breath
        super().breathe()
        #adding this to just the Fish class 
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")
# creating object from the fish class
nemo = Fish()
nemo.breathe()
print(nemo.num_eyes)
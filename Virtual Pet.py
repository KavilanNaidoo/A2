#Virtual Pet

class VirtualPet():
    def __init__(self,name):
        self.name = name
        self.energy = 50
        self.mood = 5
        self.foods = ["Biscuits"]
        self.bored = 0
        self.play = ["Ball","Walk"]

    def eat(self,food):
        if food in self.foods:
            if food == self.foods[0]:
                self.energy = self.energy + 10
                self.mood = self.mood + 1
                print("mmmmm")
            else:
                print("Im not eating that!")
                self.mood = self.mood - 1
                
    def play(self,play):
        if self.boredom > 5:
            print("Yay")
            if play in self.play:
                if play == self.play[0]:
                    self.bored = self.bored - 3
                    self.energy = self.energy - 20
                    self.mood = self.mood + 2
                elif play == self.play[1]:
                    self.bored = self.bored - 1
                    self.energy = self.energy - 10
                    self.mood = self.mood + 1
                else:
                    print("I'm not playing that!")
                    self.mood = self.mood - 1
                    self.bored = self.bored - 2
                    
                
            
            
    
    
pet_one = VirtualPet("Bob")
pet_one.eat("Biscuits")
pet_one.play("Walk")
print(pet_one.name)

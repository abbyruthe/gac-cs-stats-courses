## Programming a Pet Part 1:

import random
class Pet:
    
    # Pet(str) -> void
    def __init__ (self, name):
        """creates a Tamagotchi pet with the given name"""
        self.name = name
        self.fullness = 8
        self.happiness = 8
        self.cleanliness = 8
        self.alive = True
        self.stage = "egg"
        self.progress = 1

    # void -> void
    def feed(self):
        """adds 3 to fullness integer until 10 and then subtracts two from
        cleanliness value"""
        self.fullness += 3
        if self.fullness > 10:
             self.fullness -= 2
             self.fullness = 10
        if self.cleanliness <= 1:
             self.cleanliness = 1
             
    # void -> void
    def play(self):
        """adds 3 to happiness integer until 10 and then subtracts two from
        fullness value"""
        self.happiness += 3
        if self.happiness > 10:
             self.fullness -= 2
             self.happiness = 10
        if self.fullness <= 1:
             self.fullness = 1


    # void -> void
    def bathe(self):
        """adds 3 to cleanliness integer until 10 and then subtracts two from
        happiness value"""
        self.cleanliness += 3
        if self.happiness > 10:
             self.happiness -= 2
             self.happiness = 10
        if self.happiness <= 1:
             self.happiness = 1



    #  Pet Object -> void
    def age_up(self):
        """changes the value of stage and resets progress to 1"""
        if self.stage == "egg":
            self.stage = "baby"
        elif self.stage == "baby":
            self.stage = "child"
        elif self.stage == "child":
            self.stage = "adult"
        else:
            self.stage = "adult"
        self.progress = 1

    # void -> string
    def status(self):
        """if fullness, happiness, and cleanliness are greater than or equal to
    5, return fine, if fullness, happiness, and cleanliness are equal to or less
    than one, return dead, if fullness, happiness, and cleanliness are less than
    5 but not dead, return distress"""
        if self.fullness > 5 and self.happiness > 5 and self.cleanliness > 5:
            return "fine"
        if self.fullness == 1 or self.happiness == 0 or self.cleanliness == 0:
            self.alive = False
            return "dead"
        if  1 < self.fullness <= 5 or 1 < self.happiness <= 5 or 1 < self.cleanliness <= 5:
            return "distress"
        
    # void -> str
    def time_step(self):
        """randomly chooses one of fullness, happiness, and cleanliness to decrease
    by 1 and increase progress by 1, and returns the string status"""
        option = random.choice(["fullness", "happiness", "cleanliness"])
        if option == "fullness":
            self.fullness -= 1
            if self.fullness <= 1:
                self.fullness = 1
        if option == "happiness":
            self.happiness -= 1
            if self.happiness <= 1:
                self.fullness = 1
        if option == "cleanliness":
            self.cleanliness -= 1
            if self.cleanliness <= 1:
                self.cleanliness = 1
        self.progress += 1
        if self.progress == 20:
            self.age_up()
        return self.status()

## Diplaying the Pet Part 2:
    import cTurtle
import time

def fill_circle(turtle, color, radius, position):
        turtle.up()
        turtle.goto(position)
        turtle.down()
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()
        turtle.up()
        turtle.goto(0,0)
        
class TamagotchiGame:
    # Tamagotchi(str)
    def __init__(self, name):
        """Creates a Tamagotchi Pet with the given name"""
        self.pet = Pet(name)
        self.pen = cTurtle.Turtle()
        self.pen.up()

    def draw_egg(self):
        self.pen.tracer(0,0)
        fill_circle(self.pen, "green", 20, (0,0))
        fill_circle(self.pen, "white", 5, (10,20))
        fill_circle(self.pen, "white", 5, (-10,20))
        fill_circle(self.pen, "black", 2, (10,22))
        fill_circle(self.pen, "black", 2, (-10,22))
        self.pen.update()

    def draw_baby(self):
        self.pen.tracer(0,0)
        fill_circle(self.pen, "red", 10, (15,0))
        fill_circle(self.pen, "red", 10, (-15,0))
        fill_circle(self.pen, "red", 30, (0,0))
        fill_circle(self.pen, "white", 8, (15,30))
        fill_circle(self.pen, "white", 8, (-15,30))
        fill_circle(self.pen, "black", 4, (15,34))
        fill_circle(self.pen, "black", 4, (-15,34))
        self.pen.update()

    def draw_child(self):
        self.pen.tracer(0,0)
        fill_circle(self.pen, "purple", 14, (20,0))
        fill_circle(self.pen, "purple", 14, (-20,0))
        fill_circle(self.pen, "purple", 10, (40,40))
        fill_circle(self.pen, "purple", 10, (-40,40))
        fill_circle(self.pen, "purple", 40, (0,0))
        fill_circle(self.pen, "white", 10, (15,40))
        fill_circle(self.pen, "white", 10, (-15,40))
        fill_circle(self.pen, "black", 5, (15,44))
        fill_circle(self.pen, "black", 5, (-15,44))
        self.pen.update()

    def draw_adult(self):
        self.pen.tracer(0,0)
        fill_circle(self.pen, "blue", 18, (25,0))
        fill_circle(self.pen, "blue", 18, (-25,0))
        fill_circle(self.pen, "blue", 12, (50,50))
        fill_circle(self.pen, "blue", 12, (-50,50))
        fill_circle(self.pen, "blue", 50, (0,0))
        fill_circle(self.pen, "purple", 5, (0,35))
        fill_circle(self.pen, "white", 12, (15,50))
        fill_circle(self.pen, "white", 12, (-15,50))
        fill_circle(self.pen, "black", 6, (15,55))
        fill_circle(self.pen, "black", 6, (-15,55))
        self.pen.update()

    def draw_tombstone(self):
        self.pen.tracer(0,0)
        self.pen.fillcolor("gray")
        self.pen.begin_fill()
        self.pen.forward(50)
        for i in range(2):
            self.pen.left(90)
            self.pen.forward(200)
            self.pen.left(90)
            self.pen.forward(100)
        self.pen.end_fill()
        self.pen.up()
        self.pen.goto(0,160)
        self.pen.write("RIP", align = "center", font=("Arial", 20, "normal"))
        self.pen.goto(0,140)
        self.pen.write(self.pet.name, align = "center", font=("Arial", 15, "normal"))
        self.pen.goto(0,0)
        self.pen.update()

    def display(self):
        self.pen.clear()
        self.pen.up()
        self.pen.goto(0,-30)
        self.pen.write(self.pet.name, align = "center", font=("Arial", 20, "normal"))
        self.pen.goto(0,0)
        if self.pet.stage == "egg":
            self.draw_egg()
        elif self.pet.stage == "baby":
            self.draw_baby()
        elif self.pet.stage == "child":
            self.draw_child()
        else:
            self.draw_adult()

    def feed(self):
        self.pet.feed()
        self.display()
        self.pen.goto(0,20)
        self.pen.write("NOM NOM NOM", align = "center", font=("Arial", 30, "normal"))
        self.pen.goto(0,0)
        time.sleep(2)
        self.display()

    def play(self):
        self.pet.play()
        self.display()
        self.pen.goto(0,20)
        self.pen.write("WEEEEE!!!!!", align = "center", font=("Arial", 30, "normal"))
        self.pen.goto(0,0)
        time.sleep(2)
        self.display()

    def bathe(self):
        self.pet.bathe()
        self.display()
        self.pen.goto(0,20)
        self.pen.write("SCRUB SCRUB SCRUB", align = "center", font=("Arial", 30, "normal"))
        self.pen.goto(0,0)
        time.sleep(2)
        self.display()

    # void -> void
    def run(self):
        """Runs the Tamagotchi game"""
        self.display()
        time.sleep(2)
        state = self.pet.time_step()
        while state != "dead":
            self.display()
            if state == "distress":
                for i in range(2,5):
                    self.pen.goto(0,30*i)
                    self.pen.write("WWAHHHH!! :(", align = "center", font=("Arial", 30, "normal"))
                self.pen.goto(0,0)
            self.pen.goto(0,-50)
            self.pen.write("Type 1 to feed, 2 to play, 3 to bathe", align = "center", font=("Arial", 15, "normal"))
            self.pen.goto(0,0)
            self.pen.listen()
            self.pen.onKey(self.feed, "1")
            self.pen.onKey(self.play, "2")
            self.pen.onKey(self.bathe, "3")
            time.sleep(1)
            state = self.pet.time_step()
        self.pen.clear()
        self.draw_tombstone()
        self.pen.exitOnClick()

## Part 3: One Last Function
    # void -> void
    def greet_user():
        """prints a greeting string and asks for a user's name and prints
        greeting with user's name in it"""
        print("What is your name?")
        name = input()
        print("Hi, " + name + ", nice to meet you!")

    # void -> void
    def play_tamagotchi():
        """asks player name of their Tamagotchi and runs the game"""
        print ("What would you like to name your Tamagotchi?")
        name = input()
        game = TamagotchiGame(name)
        game.run()
    

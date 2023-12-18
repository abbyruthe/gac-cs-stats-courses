import cTurtle
import time

# turtle object, str, int, (int,int) -> void
def fill_circle(turtle, color, radius, position):
    """input provides information on filling a circle with provided radius size, colo,
    and position"""
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
    # Tamagotchi(str) -> void
    def __init__(self, name):
        """Creates a Tamagotchi Pet with the given name"""
        self.pet = Pet(name)
        self.pen = cTurtle.Turtle()
        self.pen.up()

    # void -> void
    def draw_egg(self):
        """provides details for graphics on the image of what the egg looks like
    for the Tamagotchi"""
        self.pen.tracer(0,0)
        fill_circle(self.pen, "green", 20, (0,0))
        fill_circle(self.pen, "white", 5, (10,20))
        fill_circle(self.pen, "white", 5, (-10,20))
        fill_circle(self.pen, "black", 2, (10,22))
        fill_circle(self.pen, "black", 2, (-10,22))
        self.pen.update()

    # void -> void
    def draw_baby(self):
        """draws a baby Tamagotchi"""
        self.pen.tracer(0,0)
        fill_circle(self.pen, "red", 10, (15,0))
        fill_circle(self.pen, "red", 10, (-15,0))
        fill_circle(self.pen, "red", 30, (0,0))
        fill_circle(self.pen, "white", 8, (15,30))
        fill_circle(self.pen, "white", 8, (-15,30))
        fill_circle(self.pen, "black", 4, (15,34))
        fill_circle(self.pen, "black", 4, (-15,34))
        self.pen.update()

    # void -> void
    def draw_child(self):
        """draws a child version of a Tamagotchi"""
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

    # void -> void
    def draw_adult(self):
        """draws an adult version of a Tamagotchi"""
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

    # void -> void
    def draw_tombstone(self):
        """draws a tombstone for the Tamagotchi when it dies"""
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

    # void -> void
    def display(self):
        """formats the name of the pet on the screen along with what the stage
        the pet is at, also draws the pet in said stage in turtle"""
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

    # void -> void
    def feed(self):
        """provides captions for while the pet is eating as well as formatting
        the words"""
        self.pet.feed()
        self.display()
        self.pen.goto(0,20)
        self.pen.write("NOM NOM NOM", align = "center", font=("Arial", 30, "normal"))
        self.pen.goto(0,0)
        time.sleep(2)
        self.display()

    # void -> void
    def play(self):
        """provides a caption for while the pet is playing as well as formatting
        the words"""
        self.pet.play()
        self.display()
        self.pen.goto(0,20)
        self.pen.write("WEEEEE!!!!!", align = "center", font=("Arial", 30, "normal"))
        self.pen.goto(0,0)
        time.sleep(2)
        self.display()

    # void -> void
    def bathe(self):
        """provides a caption for while the pet is bathing as well as formatting
        the words"""
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
        
    


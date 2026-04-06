from utils import *

set_background("underwater")


x1 = -205
y1 = 209
x2 = -205
y2 = 25
x3 = -205
y3 = -107
x4 = -205
y4 = -205

c1 = create_sprite("character1", x1, y1)
c2 = create_sprite("character2", x2, y2)
c3 = create_sprite("fish_big", x3, y3)
c4 = create_sprite("fish", x4, y4)

time.sleep(10)

# Changing x values for sprites are random so that the winner is unknown
for i in range(30):
    x1 += random.randint(0, 56)
    x2 += random.randint(0, 56)
    x3 += random.randint(0, 56)
    x4 += random.randint(0, 56)


    c1.goto(x1, y1)
    c2.goto(x2, y2)
    c3.goto(x3, y3)
    c4.goto(x4, y4)

    window.update()
    time.sleep(0.3)

time.sleep(2)

s5 = create_sprite("alien",-200,-106)
s5.color("Yellow")

time.sleep(2)


if x1 >= x2 and x1 >= x3 and x1 >= x4:
    s5.write("Player 1 wins!",font = ("Arial", 25, "normal"))
    time.sleep(5)
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    s5.write("player 2 wins!",font = ("Arial", 25, "normal"))
    time.sleep(5)
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    s5.write("Player 3 wins!",font = ("Arial", 25, "normal"))
    time.sleep(5)
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
    s5.write("Player 4 wins!",font = ("Arial", 25, "normal"))
    time.sleep(5)
    

    
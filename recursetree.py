import random
import turtle

def tree(branchLen,t):
    ang = random.randint(15,45)
    if branchLen > 5:
        t.forward(branchLen)
        t.width(5)
##        t.pensize(3)
        t.right(ang) 
        tree(branchLen-15,t)
        t.left(ang*2)
        t.color("green")
        tree(branchLen-15,t)
        t.right(ang)
        t.backward(branchLen)
        t.color("brown")

def main():
    ang = random.randint(15,45)
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.width(7)
##    t.pensize(7)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    tree(110,t)
    myWin.exitonclick()

main()

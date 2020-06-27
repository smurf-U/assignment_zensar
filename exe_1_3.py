import turtle 
turtle.hideturtle()

  
s = 100
  
col = '#fff'

t1 = turtle.Turtle() 
t1.hideturtle()
r = 50

t1.circle(r) 


t = turtle.Turtle() 
t.hideturtle()
t.fillcolor(col) 
# t.setx(125)
# t.sety(125)
for _ in range(6): 
  t.forward(s) 
  t.right(-60)

t2 = turtle.Turtle() 
t2.hideturtle()
t2.fillcolor(col) 
# t.setx(125)
# t.sety(125)
for _ in range(4): 
  t2.forward(25) 
  t2.right(-90)


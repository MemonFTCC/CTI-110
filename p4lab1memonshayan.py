# shayan memon
# 3/19/2025
# p4lab1
# Turtle Graphics program to draw triangle and sqaure

import turtle
win = turtle.Screen() 
sam = turtle. Turtle()


#set the way sam looks
sam.pensize(6)
sam.pencolor('blue')
sam.shape('arrow')

# test
# sam.forward(100)

# for loop that runs 4 times
for i in range (4):
    sam.forward(100)
    sam.right(90)



# While loop that runs 3 times
this_run = 0 


while this_run < 3: 
 sam.forward(100)
 sam.left(120)
 this_run +=1 









# keeps the window open
win.mainloop()





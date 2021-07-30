import curses

#Initialize Screen
curses.initscr()

#Define Window Dims (y,x)
# X,Y coordinates are inverted throughout the program 
# because of how they were defined in the Lib-Curses 
# So, X,Y= Y,X. Only vertically.        
win=curses.newwin(20,60,0,0)            

#Use arrow keys
win.keypad(1)             

#Don't listen to other input characters and print
curses.noecho()           

#Cursor Visibility (Toggle- 0 or 1)
curses.curs_set(0)            

#Border around the window
win.border(0)             

#Not waiting for another user input to display result
win.nodelay(1)            

#Snake and food
#Starting/Init Coordinates
snake=[(4,10),(4,9),(4,8)]
food=(10,20)

#Coordinates of Food, Represented by the symbol '#'
win.addch(food[0],food[1],"#")

#Game Logic
score=0

ESC=27
key= curses.KET_RIGHT
arrow_keys=[curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]

while key!=ESC: 
    win.addstr(0,2,'Score: '+ str(score)+ '')  # Add score to the screen 
    win.timeout(150 -(len(snake)) //5 + len(snake)//10 %120)  #Code to increase the speed of the snake every time it eats food

    prev_key=key
    event=win.getch() #Get next Character
    key=event if event !=-1 else prev_key #Check if no other key is pressed   

    if key not in arrow_keys: #Check if key pressed in not in arrow keys and escape
        key= prev_key

    #Calculate the next coordinates of snake
    y=snake[0][0]    
    x=snake[0][1]
    if key== curses.KEY_DOWN:
        y += 1
    if key==curses.KEY_UP:
        y -= 1
    if key==curses.KEY_LEFT:
        x -= 1
    if key==curses.KEY_RIGHT:
        x += 1

    snake.append(0, (y,x)) #Use .append instead of .insert as Append is faster O(1) and Insert takes O(n) because it has to shift everything to the right

    #Check if we it the border(0) or the last row(19) or column(59)
    if y==0: break
    if y==19: break
    if x==0: break
    if x==59: break

    #Check if snake runs over itself or eats itself
    #snake[0] means the head in snake[1:]- the body of the snake. So, if snake's head coords inside the body coords.
    if snake[0] in snake[1:]: break

    #If snake eats the food, increase the score by one
    if snake[0] == food:
        score+=1
        #create new food at new loc
        food= ()


    for c in snake:
        win.addch(c[0],c[1], "*")    #Coordinates of the Snake on the Screen. Snake represented by "*"

curses.endwin() #End window session
print(f"Final Score:{score}")
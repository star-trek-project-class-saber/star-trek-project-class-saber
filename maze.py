# star-trek-project-class-saber
CSCI 121

from Myro import*

def move():
 
    while True:
        getLine()
        
        #Just in case, for whatever reason, the robot is still on the line
        if getLine("left") == 1 or getLine("right") == 1:
            forward(.5,1)
            turnBy(90)
            continue
            
        else:
            startTime = currentTime()
            elaspedTime = currentTime() - startTime
    
            while (elaspedTime < 3) and (left == 0 or right == 0):        
                backward(.4)
                elaspedTime = currentTime() - startTime
                
                if (elaspedTime <= 3) and (getLine("left") == 1 or getLine("right") == 1):
                    forward(.5,1)
                    turnLeft(.5,1.3)
                    break
                
                elif(elaspedTime >= 3):    
                    turnRight(.5,1.3)
            
            
move()

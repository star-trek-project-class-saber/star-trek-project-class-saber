# star-trek-project-class-saber
CSCI 121

from Myro import*

def move():
    
    currentLight=getLight()

    while True:
        getLine()

        #light sensor
        elapsedLight=getLight()
        
        if currentLight[0]-elapsedLight[0]>10000 or currentLight[1]-elapsedLight[1]>10000 or currentLight[2]-elapsedLight[2]>10000 :
            turnRight(1,1.2)
            pic=takePicture()
            show(pic)
            #save(pic)
            turnRight(1,.2)
            pic=takePicture()
            show(pic)
            #save(pic)
            turnRight(1,.2)
            pic=takePicture()
            show(pic)
            #save(pic)
            turnRight(1,1.1)
            elapsedLight=getLight()
        
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

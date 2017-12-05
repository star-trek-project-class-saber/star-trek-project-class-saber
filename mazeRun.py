from Myro import*



def move(time,speed):
    left = getLine("left")
    right = getLine("right")
    
    while (getLine("left") == 0 or getLine("right")):
       startTime = currentTime()
       elaspedTime = currentTime() - startTime
       backward(speed)
        
       if getLine("left") == 1 or getLine("right") == 1:
            forward(speed,1)
            turnBy(90)   
            break
    
    
    
    startTime = currentTime()
    elaspedTime = currentTime() - startTime
    count = 0        
            
    while True:
        backward(speed)
           
        
        elaspedTime = currentTime() - startTime
        if (elaspedTime <= time) and (getLine("left") == 1 or getLine("right") == 1):
            forward(speed,1)
            turnBy(90)
            count = 0
            startTime = currentTime()
            continue
                
        elif(elaspedTime >= time):  
            stop()
            if count == 3:
                turnBy(90)
                count = 0
            else:  
                turnBy(-90)
                count += 1
            
            startTime = currentTime()
            continue
                    
        elif getIR("left") == 0 or getIR("right") == 0: 
            stop()
            turnBy(90)
            count = 0
            startTime = currentTime()


        elif getLight("left")<50000 or getLight("center")<50000 or getLight("right")<50000 :
            turnRight(1,1.2)
            pic=takePicture()
            show(pic)
            turnRight(1,1.5)
                      
              
move(3,.6)

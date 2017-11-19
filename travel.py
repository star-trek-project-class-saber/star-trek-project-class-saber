#Thid code can line checking per 1 sec.
#When scrribler meet line at front, it turn left.

#This code can't line checking when right side has no line.
def travel():
    while(getLine("left")==0):#until meeting front line
        backward(.5,1) #go 1 sec
        turnBy(-90) #and turn right
        while(getLine("left")==0): #until meetin right line
            backward(.3) #go
        forward(.3,1) #if meet line go back 1 sec
        turnBy(90) #and turn left
    forward(.3,2) #if it meet line at front
    turnBy(90) # turn left
    travel() #agian
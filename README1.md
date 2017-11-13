# star-trek-project-class-saber
CSCI 121

from Myro import*

def test():
    startTime = currentTime()
    
    while True:
        getLine()
        if getLine("left") == 1 or getLine("right") == 1:
            forward(.6,1)
            turnBy(90)
            continue
        else:
            backward(.6)
        
    stop()
test()

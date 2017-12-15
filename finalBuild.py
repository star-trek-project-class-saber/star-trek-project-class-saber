from Myro import*

import random

import urllib2

def normalize(v):
    ambient = sum(getLight())/3
    if v > ambient:
        v = ambient
    return 1.0 - v/ambient
    
           
def findLine(speed):
    while True:
            

        startTime = currentTime()
        elaspedTime = currentTime() - startTime
        backward(speed)
                
        if getLine("left") == 1 or getLine("right") == 1:
            forward(.5,1)
            turnBy(90)   
            break
        
        elif getIR("left") == 0 or getIR("right") == 0:
            stop()
            turnBy(90)
            break

    startTime = currentTime()
    elaspedTime = currentTime() - startTime
    count = 0
    
def move(speed,time):
               
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
            break
            
        elif (elaspedTime >= time):
            stop()
            break                    
            
            
            
            
            

def postImage(url,fileName):
    body= '';

    try:
        file = open(fileName,'rb')
        body = file.read()
        file.close()
    except OSError:
        return b''

    part_boundary = b'---------------------Boundary'+bytes(str(int(random.random()*1e10)),'utf-8')
    data = []
    data.append(b'--'+part_boundary)
    data.append(bytes('Content-Disposition: form-data; name="file"; filename="{}"'.format(fileName),'utf-8'))
    data.append(bytes('Content-Type: {}'.format('image/png'),'utf-8'))
    data.append(b'')
    data.append(body)
    data.append(b'--' + part_boundary + b'--')
    data.append(b'')
    body = b''

    for item in data:
        body += item + b'\r\n'

    request = urllib2.Request(url)
    # adding charset parameter to the Content-Type header.
    request.add_header("Content-Type","multipart/form-data;boundary={}".format(str(part_boundary)))
    request.add_header('Content-length', len(body))
    webHandle = urllib2.urlopen(request,body)
    reply = webHandle.read();
    webHandle.close()
    return reply

def deleteCommand(url):

    request = urllib2.Request(url)
    request.get_method = lambda: 'DELETE'
    webHandle = urllib2.urlopen(request)
    command = webHandle.read();
    webHandle.close()
    return command

def getCommand(url):

    request = urllib2.Request(url)
    webHandle = urllib2.urlopen(request)
    command = webHandle.read();
    webHandle.close()
    return command

def sendPicToServer(picName):

    url ='http://localhosts:8080/robot'
    postImage(url,picName)
    cmdInJSONFormat = getCommand(url) # example command get
    cmdOutJSONFormat = deleteCommand(url) # example command delete
    print(cmdInJSONFormat)

class Saber:
    def __init__(self,speed = .5, time = 3):
        self.speed = speed
        self.time = time
        
    def search(self):
        for i in range(18):
            
                turnBy(20)
                pic=takePicture()
                show(pic)
                picName='picture.jpg'
                savePicture(pic,picName)
                #sendPicToServer(picName)
                url ='http://localhost:8080/robot'

                postImage(url,picName)
                cmdInJSONFormat = getCommand(url)
                print(cmdInJSONFormat)
    
    def naviMaze(self):
        left = getLine("left")
        right = getLine("right")
        MOVE = 1
        CHECK_WALL = 2
        SEARCH_LIGHT = 3
        FOUND_WALL = 4
        
        otherState = FOUND_WALL
        currentState = MOVE
        
        findLine(self.speed)
        
        startTime = currentTime()
        count = 0
        light = False
                
        while light == False:

            backward(self.speed) 
            
            elaspedTime = currentTime() - startTime
            
            if (getLine("left") == 1 or getLine("right") == 1):
                
                if currentState == CHECK_WALL or currentState == MOVE:
                    forward(.5,1)
                    turnBy(90)
                    count = 0
                    currentState = MOVE
                    if (getLine("left") == 1 or getLine("right") == 1):
                        forward(.5,1)
                        turnBy(90)
                    startTime = currentTime()
                    continue
                    
            elif(elaspedTime >= self.time):
            
                
                if (getLine("left") == 1 or getLine("right") == 1):
                    forward(.5,1)
                    turnBy(90)
                    count = 0
                    startTime = currentTime()
                    continue
                elif currentState == MOVE:  
                    stop()
                    turnBy(-90)
                    currentState = CHECK_WALL
                    count+=1
                    startTime = currentTime()
                    continue
                        
                else:
                    if count == 1:
                        stop()
                        turnBy(-90)
                        count = 0
                        startTime = currentTime()
                        continue
                
                
            elif normalize(30000) < .49:
                if otherState == SEARCH_LIGHT:
                    light = True
                    stop()
                    speak("found light")
                    turnBy(180)
                    pic=takePicture()
                    show(pic)
                    picName= 'picture.jpg'
                    savePicture(pic,picName)
                    #sendPicToServer(picName)
                    
                    for i in range(23):
                    
                        turnBy(15)
                        pic=takePicture()
                        show(pic)
                        picName='picture.jpg'
                        savePicture(pic,picName)
                       # sendPicToServer(picName)
                        url ='http://localhost:8080/robot'
                        postImage(url,picName)
                    backward(.2,.4)
                    cmdInJSONFormat = getCommand(url)

                    print(cmdInJSONFormat)
                        
                    turnBy(180)
                    break
                
                
            elif (getIR("left") == 0 or getIR("right") == 0): 
                
                
                if otherState == FOUND_WALL:
                    stop() 
                    backward(.5,1.5)
                    turnBy(90)
                    backward(.5,3.5)
                    if (getLine("left") == 1 or getLine("right") == 1):
                        forward(.5,1)
                        turnBy(-90)
                    turnBy(-90)
                    backward(.8,4)
                    if (getLine("left") == 1 or getLine("right") == 1):
                        forward(.5,1)
                        turnBy(-90)
                    turnBy(-90)
                    count = 0
                    otherState = SEARCH_LIGHT
                    currentState = CHECK_WALL
                    startTime = currentTime()
                    

 
url ='http://localhost:8080/robot'
cmdInJSONFormat = getCommand(url)

print(cmdInJSONFormat)
cmdInJSONFormat = deleteCommand(url)
go = Saber(.5,3.5)
#go.search()
go.naviMaze()

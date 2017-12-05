from Myro import*

import random
import urllib2


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
    url ='http://localhost:8080/robot'
    postImage(url,picName)
    cmdInJSONFormat = getCommand(url) # example command get
    #cmdOutJSONFormat = deleteCommand(url) # example command delete
    print(cmdInJSONFormat)


def move(time,speed):
    left = getLine("left")
    right = getLine("right")
    
    while (getLine("left") == 0 or getLine("right")==0):
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
        print(getLight())   
        
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
            stop()
            turnBy(160)
            pic=takePicture()
            show(pic)
            picName='picture.jpg'
            savePicture(pic,picName)
            #sendPicToServer(picName)
            url ='http://localhost:8080/robot'
            
            postImage(url,picName)
            cmdInJSONFormat = getCommand(url)
            print(cmdInJSONFormat)
            
            turnBy(-160)
                      
              
move(3,.6)
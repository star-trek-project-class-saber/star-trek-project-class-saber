# star-trek-project-class-saber
CSCI 121
# add light
# add server

from Myro import*
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

           
def move():
    
    currentLight=getLight()
    num=1
    picName='photo#%s.jpg'%format(num)
    url ='http://localhost:8080/robot'

    while True:
        getLine()

        #light sensor
        elapsedLight=getLight()
        
        if currentLight[0]-elapsedLight[0]>10000 or currentLight[1]-elapsedLight[1]>10000 or currentLight[2]-elapsedLight[2]>10000 :
            turnRight(1,1.2)
            pic=takePicture()
            show(pic)
            savePicture(pic,picName)
            sendPicToServer(picName)
            num+=1
            picName='photo#%s.jpg'%format(num)
           
            turnRight(1,1.5)
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

import cv2
import torch.hub
import os
import model
from PIL import Image
from torchvision import transforms
from grad_cam import BackPropagation
import time 
import requests
from twilio.rest import Client
import urllib.request
import json
import pygame

# Alarm sound file
file = 'alarm.mp3'
# Sound player start
pygame.init()
pygame.mixer.init()

# Crash Sensibility
sens=30

# Sending SMS if Crash Detected

def send():
    # Your Account SID from twilio.com/console
    account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXxx"
    # Your Auth Token from twilio.com/console
    auth_token  = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxx"
    client = Client(account_sid, auth_token)
    phone = "+XXXXXXXXXXXX"
    print('crash')
    send_url = 'http://ip-api.com/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    text="The Driver Crash Here: "
    text+="http://maps.google.com/maps?q=loc:{},{}".format(j['lat'],j['lon'])
    print(text)
    message = client.messages.create(to=phone, from_="+XXXXXXXXXXXXx",body=text)
    print(message.sid)
    time.sleep(10)
    stop()

timebasedrow= time.time()
timebasedis= time.time()
timerundrow= time.time()
timerundis= time.time()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 
MyModel="BlinkModel.t7"

shape = (24,24)
classes = [
    'Close',
    'Open',
]

eyess=[]
cface=0

def preprocess(image_path):
    global cface
    transform_test = transforms.Compose([
        transforms.ToTensor()
    ])
    image = cv2.imread(image_path['path'])    
    faces = face_cascade.detectMultiScale(
        image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(1, 1),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    if len(faces) == 0:
        ...
    else:
        cface=1
        (x, y, w, h) = faces[0]
        face = image[y:y + h, x:x + w]
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)
        roi_color = image[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(face,1.3, 10) 
        i=0
        for (ex,ey,ew,eh) in eyes:
            (x, y, w, h) = eyes[i]
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            eye = face[y:y + h, x:x + w]
            eye = cv2.resize(eye, shape)
            eyess.append([transform_test(Image.fromarray(eye).convert('L')), eye, cv2.resize(face, (48,48))])
            i=i+1
    cv2.imwrite('display.jpg',image) 
    

def eye_status(image, name, net):
    img = torch.stack([image[name]])
    bp = BackPropagation(model=net)
    probs, ids = bp.forward(img)
    actual_status = ids[:, 0]
    prob = probs.data[:, 0]
    if actual_status == 0:
        prob = probs.data[:,1]

    #print(name,classes[actual_status.data], probs.data[:,0] * 100)
    return classes[actual_status.data]

def func(imag,modl):
    drow(images=[{'path': imag, 'eye': (0,0,0,0)}],model_name=modl)

def drow(images, model_name):
    global eyess
    global cface
    global timebasedrow
    global timebasedis
    global timerundrow
    global timerundis
    net = model.Model(num_classes=len(classes))
    checkpoint = torch.load(os.path.join('Model', model_name), map_location=torch.device('cpu'))
    net.load_state_dict(checkpoint['net'])
    net.eval()
    
    flag =1
    status=""
    for i, image in enumerate(images):
        if(flag):
            preprocess(image)
            flag=0
        if cface==0:
            image = cv2.imread("display.jpg")
            image = cv2.putText(image, 'No face Detected', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.imwrite('display.jpg',image)
            print("No face Detected")
            timebasedrow= time.time()
            timebasedis= time.time()
            timerundrow= time.time()
            timerundis= time.time()
        elif(len(eyess)!=0):
            eye, eye_raw , face = eyess[i]
            image['eye'] = eye
            image['raw'] = eye_raw
            image['face'] = face
            timebasedrow= time.time()
            timerundrow= time.time()
            for index, image in enumerate(images):
                status = eye_status(image, 'eye', net)
                if(status =="Close"):
                    print("Distracted")
                    timerundis= time.time()
                    pygame.mixer.music.load(file)
                    pygame.mixer.music.play()
                    if((timerundis-timebasedis)>2):
                        image = cv2.imread("display.jpg")
                        image = cv2.putText(image, 'Distracted', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                        cv2.imwrite('display.jpg',image)
                
                else:
                    timebasedis= time.time()
                    pygame.mixer.music.stop()
        else:
            timerundrow= time.time()
            if((timerundrow-timebasedrow)>1):
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
                image = cv2.imread("display.jpg")
                image = cv2.putText(image, 'Drowsy', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                cv2.imwrite('display.jpg',image)
                print("Drowsy")

def main():
    global eyess
    global cface    
    eyess=[]
    cface=0
    ret, img = cap.read() 
    cv2.imwrite('img.jpg',img) 
    func('img.jpg',MyModel)

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    timebasedrow= time.time()
    timebasedis= time.time()
    timerundrow= time.time()
    timerundis= time.time()
    while 1:
        
        main()
        img = cv2.imread("display.jpg")
        scale_percent = 50 # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        cv2.imshow('image',img) 
        k = cv2.waitKey(30) & 0xff
        


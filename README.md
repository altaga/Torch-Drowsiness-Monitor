# Torch-Drowsiness-Monitor

The problem of drowsiness when handling or performing tasks such as driving or handling heavy machinery and the blind spot when driving.

<img src="https://i.ibb.co/1MC19TG/Logo.png" width="1000">

# Table of contents

* [Introduction](#introduction)
* [Materials](#materials)
* [Connection Diagram](#connection-diagram)
* [Jetson Setup](#jetson-setup)
* [Drowsiness Monitor](#drowsiness-monitor)
* [Blind Spot Monitor](#blind-spot-monitor)
* [The Final Product](#the-final-product)
* [Commentary](#commentary)
* [References](#references)

# Introduction:

We will be tackling the problem of drowsiness when handling or performing tasks such as driving or handling heavy machinery and the blind spot when driving.

The Center for Disease Control and Prevention (CDC) says that 35% of American drivers sleep less than the recommended minimum of seven hours a day. It mainly affects attention when performing any task and in the long term, it can affect health permanently.

<img src="https://www.personalcarephysicians.com/wp-content/uploads/2017/04/sleep-chart.png" width="1000">

According to a report by the WHO (World Health Organization) (2), falling asleep while driving is one of the leading causes of traffic accidents. Up to 24% of accidents are caused by falling asleep, and according to the DMV USA (Department of Motor Vehicles) (3) and NHTSA (National Highway traffic safety administration) (4), 20% of accidents are related to drowsiness, being at the same level as accidents due to alcohol consumption with sometimes even worse consequences than those.

<img src="https://media2.giphy.com/media/PtrhzZJhbEBm8/giphy.gif" width="1000">

# Solution:

We will create a system that will be able to detect a person's drowsiness level, this with the aim of notifying the user about his state and if he is able to drive.

At the same time it will measure the driver’s attention or capacity to garner attention and if he is falling asleep while driving. If it positively detects that state (that he is getting drowsy), a powerful alarm will sound with the objective of waking the driver.

<img src="https://i.gifer.com/origin/7d/7d5a3e577a7f66433c1782075595f4df_w200.gif" width="1000">

Additionally it will detect small vehicles and motorcycles in the automobile’s blind spots.

<img src="https://thumbsnap.com/s/Wy5w7JPR.jpg?1205" width="1000">

In turn, the system will have an accelerometer to generate a call to the emergency services if the car had an accident to be able to attend the emergency quickly.

Current Solutions:

- Mercedes-Benz Attention Assist uses the car's engine control unit to monitor changes in steering and other driving habits and alerts the driver accordingly.

- Lexus placed a camera in the dashboard that tracks the driver's face, rather than the vehicle's behavior, and alerts the driver if his or her movements seem to indicate sleep.

- Volvo's Driver Alert Control is a lane-departure system that monitors and corrects the vehicle's position on the road, then alerts the driver if it detects any drifting between lanes.

- Saab uses two cameras in the cockpit to monitor the driver's eye movement and alerts the driver with a text message in the dash, followed by a stern audio message if he or she still seems sleepy.

As you can see these are all premium brands and there is not a single plug and play system that can work for every car. This, is our opportunity as most cars in the road are not on that price range and do not have these systems.

# Materials:

Hardware:
- NVIDIA Jetson Nano.                                x1.
https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-nano/
- Power Inverter for car.
https://www.amazon.com/s?k=power+inverter+truper&ref=nb_sb_noss_2
- ESP32.
https://www.adafruit.com/product/3405
- OLED display.
https://www.amazon.com/dp/B072Q2X2LL/ref=cm_sw_em_r_mt_dp_U_TMGqEb9YAGJ5Q
- Any Speaker
https://www.amazon.com/s?k=speaker&s=price-asc-rank&page=2&qid=1581202023&ref=sr_pg_2
- USB TP-Link USB Wifi Adapter TL-WN725N.            x1.
https://www.amazon.com/dp/B008IFXQFU/ref=cm_sw_em_r_mt_dp_U_jNukEbCWXT0E4
- Any External USB Audio Adapter Sound Card.         x1.
https://www.amazon.com/s?k=usb+sound+card+adapter&crid=2ESMWR4SXL4CD&sprefix=usb+sound+ca%2Caps%2C210&ref=nb_sb_ss_i_1_12
- Logitech HD Laptop Webcam C615.                    x1.
https://www.amazon.com/dp/B004YW7WCY/ref=cm_sw_em_r_mt_dp_U_8OukEbBJGXVNX
- HD webcam                      .                   x1.
https://canyon.eu/product/cne-cwc2/
- 32 GB MicroSD Card.                                x1.
https://www.amazon.com/dp/B06XWN9Q99/ref=cm_sw_em_r_mt_dp_U_XTllEbK0VKMAZ
- 5V-4A AC/DC Adapter Power Supply Jack Connector.   x1.
https://www.amazon.com/dp/B0194B80NY/ref=cm_sw_em_r_mt_dp_U_ISukEbJN7ABK3
- USB Hub.                                           x1.
https://www.amazon.com/s?k=usb+hub&ref=nb_sb_noss_1
- VMA204.                                            x1.
https://www.velleman.eu/products/view?id=435512

Software:
- Pytorch:
https://pytorch.org/
- JetPack 4.3:
https://developer.nvidia.com/jetson-nano-sd-card-image-r3231
- YOLOv3:
https://pjreddie.com/darknet/yolo/
- OpenCV:
https://opencv.org/
- Twilio:
https://www.twilio.com/
- Arduino IDE:
https://www.arduino.cc/en/Main/Software
- Mosquitto MQTT:
https://mosquitto.org/

# Connection Diagram:

This is the connection diagram of the system:

<img src="https://i.ibb.co/0DJTFs4/Scheme.png" width="800">

# Jetson Nano Setup:

## SD card Setup:

To download the operating system of the Jetson Nano enter the following link:

https://developer.nvidia.com/jetson-nano-sd-card-image

Format the SD card with SD Card Formatter and Flash the operating system in the SD with Etcher.

Video: Click on the image
[![Setup](https://i.ibb.co/jRBdzqS/Logo.png)](https://youtu.be/CJcYq71qwTE)

## Hardware Setup:

Because we will be using several hardware components such as cameras, an accelerometer, speakers and more, I highly recommend a power supply of at least 5V - 4A.

The only hardware device that is not plug and play is the accelerometer because this one uses a I2C protocol (TWI if you speak Atmel). That's why we have to check if the Jetson Nano has these pins available.

<img src="https://i.ibb.co/5x6bsWJ/bus.png" width="800">

In this case we will use the Bus 1 because of its proximity to the 5V and GND pins. This will allow us to create a soldered circuit like an Arduino shield, but this time for the Jetson Nano.

<img src="https://i.ibb.co/BP47wYY/Esquema-bb.png" width="800">

After soldering our circuit looks like so:

<img src="https://i.ibb.co/vh2rHtm/mod1.jpg" width="800">
<img src="https://i.ibb.co/mHJYnQM/mod02.jpg" width="800">

This next video show us how to setup our hardware:

Video: Click on the image
[![Setup](https://i.ibb.co/1MC19TG/Logo.png)](https://youtu.be/a8YcOPVFyD8)

Curious Fact: The Nvidia Jetson Nano has the same IO pin distribution as a Raspberry Pi, so every shield for the Pi is backwards compatible with the Nano!

## WiFi Setup:

The device has to be first set up with a WiFi connection, because of the fact that there are a ton of libraries we have to install. During the boot portion of the OS installation, we will connect the Jetson to your private WiFi and next we will set up the WiFi from our mobile phone (For this project as we need a Cellular connection). The advantage of doing this is that the Nano will connect to the one available so we can easily control this from the outside. TLDR: Connect both your private WiFi and your Mobile phone during the first setup, you the system can recognize both automatically.

Boot WiFi:

<img src="https://i.ibb.co/mz9tbYq/Jetson-Wi-Fi-Boot.png" width="800">

Home WiFi IP:

IP: 192.168.0.23

<img src="https://i.ibb.co/dL0nTsf/image.png" width="800">

Mobile WiFi:

IP: 192.168.43.246

<img src="https://i.ibb.co/y5HZm42/Ip-Phone-New.png" width="800">

## Software Setup:

We need to access our jetson from any command terminal via SSH, in the case of MAC and Linux just open the terminal and type the following command.

    ssh youruser@yourip

The command that I use in MY case is:

    ssh alex@192.168.0.23

In Window's case you can access it from any SSH connection assistant such as Putty.

https://www.putty.org/

## Twilio Setup

### Create Account

Open a twilio account to be able to notify via SMS in case of a crash.

https://www.twilio.com/try-twilio

### Obtain your credentials

The credentials for the Python code appear immediately upon entering, save the SID and the token, we will configure them later.

<img src="https://i.ibb.co/4MjwrBH/twilio.png" width="1000">

### Verify your Personal Phone Number

When you signed up for your trial account, you verified your personal phone number. You can see your list of verified phone numbers on the Verified Caller IDs page.

Go to your Verified Caller IDs page in the console.

<img src="https://twilio-cms-prod.s3.amazonaws.com/images/find_phone_nums_dash.width-500.png" width="300">

<img src="https://twilio-cms-prod.s3.amazonaws.com/images/find_verified_callerIDs_link.width-500.png" width="1000">

Click on the red plus (+) icon to add a new number.

<img src="https://twilio-cms-prod.s3.amazonaws.com/images/verified_caller_ids_page.width-800.png" width="1000">

Enter the phone number you wish to receive the notification from Twilio. 

<img src="https://twilio-cms-prod.s3.amazonaws.com/images/verify_phone_num.width-500.png" width="1000">

**Note: You will need access to this device to receive the call or text with your verification code**

Enter the verification code. You’re now ready to text or call this number with your trial Twilio account.

<img src="https://twilio-cms-prod.s3.amazonaws.com/images/phone_verification_code.width-500.png" width="1000">

### Get Twilio Phone Number

Go to Phone Numbers page in the console.

<img src="https://twilio-cms-prod.s3.amazonaws.com/images/find_phone_nums_dash.width-500.png" width="300">

Go to Getting Started page in the console and click on "Get your first Twilio phone number".

<img src="https://twilio-cms-prod.s3.amazonaws.com/images/get_your_trial_number.width-800.png" width="1000">

A number will be automatically offered, save this number for later and press "Choose this number" to finish setting up your number.

<img src="https://twilio-cms-prod.s3.amazonaws.com/images/Screen_Shot_2017-11-30_at_8.49.18_AM.width-800.png" width="1000">

## Mosquitto MQTT setup

Create your own Mosquitto MQTT.

https://mosquitto.org/

<img src="https://mosquitto.org/images/mosquitto-text-side-28.png" width="1000">

## Setup boot start scripts

In order for both files to run at the same time on the device's boot, we must run the following commands to create an rc.local file and give it the permission to run both scripts.

    cd
    sudo mv "Jetson-Drowsiness-Driving-Monitor/Config File/rc.local" /etc/rc.local
    sudo chmod u+x /etc/rc.local

The rc.local content is:

    #!/bin/bash

    sleep 10

    sudo python3 "Jetson-Drowsiness-Driving-Monitor/Python Scripts/Drowsiness.py" &
    sudo python3 "Jetson-Drowsiness-Driving-Monitor/Python Scripts/Yolo.py" &


# ESP32 Setup

Schematics of the OLED (128x32) and the ESP32.

<img src="https://i.ibb.co/n8G4Yk1/Oled.png" width="1000">

I grabbed a case and fit everything inside and this is how it looks:

<img src="https://i.ibb.co/WxqDyqB/1.jpg" width="1000">
<img src="https://i.ibb.co/qn3n70n/20200210-200045.jpg" width="1000">

These are the images it will show according to the CV detection, whether it sees a bike or a dog or anything else:

<img src="https://i.ibb.co/Htrf0Bm/20200210-203851.jpg" width="400"><img src="https://i.ibb.co/TRCLzjv/20200210-203909.jpg" width="400">
<img src="https://i.ibb.co/FmnvLtw/20200210-203826.jpg" width="400"><img src="https://i.ibb.co/dMcL9gn/20200210-203839.jpg" width="400">

If you want to add more images to the display, you have to use the following image2cpp converter, which will convert pixels into a code that Arduino IDE can use:

https://javl.github.io/image2cpp/

The web application gives us the code to copy and paste in our arduino project.

The device code is in the "Arduino" folder and all we have to do is configure the WiFi and MQTT credentials.

<img src="https://i.ibb.co/x2KRmKM/image.png" width="1000">

# Drowsiness Monitor:

Let's go through a revision of the algorithms and procedures of both CV systems (Drowsiness and alert on one side and Blind spot detection on the other). The installation is remarkably easy as I have already provided an image for the project.

ALL the code is well explained in the respective Github file: https://github.com/AlexSanch/Jetson-Drowsiness-Driving-Monitor

Look for the two Python files: Drowsiness and Yolo:

https://github.com/AlexSanch/Jetson-Drowsiness-Driving-Monitor/blob/master/Python%20Scripts/Drowsiness.py

https://github.com/AlexSanch/Jetson-Drowsiness-Driving-Monitor/blob/master/Python%20Scripts/Yolo.py

Those are the two that make all the magic happen.

Please take a look at it for extensive explanation and documentation.

The sleep monitor uses the following libraries:

- OpenCV:
- Image processing
    - Haarcascades implementation.
    - Flashing speed detection.
- Pygame: 
    - Player sound alert.
- Smbus:
    - Accelerometer reading.
- Twilio:
    - Emergency notification delivery.
- Requests:
    - Geolocation

The flicker detection algorithm is as follows:

- Detection that there is a face of a person behind the wheel:

<img src="https://i.ibb.co/ZMvwvfp/Face.png" width="600">

- If a face is detected, perform eye search.

<img src="https://i.ibb.co/StK0t2x/Abiertos.png" width="600">

- Thanks to the sensitivity of the Haarcascades we can use that in our favor. If a scaleFactor = 1.1 and minNeighbors = 40 is selected we can detect eyes only if the person has them open.

<img src="https://i.ibb.co/j4RQSdv/Cerrados.png" width="600">

- Because a blink lasts approximately 350 milliseconds then a single blink will not cause problems, however once the person keeps blinking for more than 2 or 3 seconds (according to our criteria) it will mean for the system that the person is falling asleep. Not separating the eyes from the road being one of the most important rules of driving.

<img src="https://i.ibb.co/kQ12W79/alert1.png" width="600">
<img src="https://i.ibb.co/LdVD7v2/alert2.png" width="600">

- Also during the demo I found a very interesting use case, when one turns to look at his cell phone, the system also detects that you are not seeing the road. This being a new aspect that we will be exploring in future versions of the system to improve detection when a driver is not looking at the road and is distracted. But, for now it is one of those unintended great finds.

<img src="https://i.ibb.co/mHZ4VdX/Cel.png" width="600">
<img src="https://i.ibb.co/3k512YS/cel2.png" width="600">

# Blind Spot Monitor:

The blind Spot monitor uses the following libraries:

- OpenCV:
    - Image processing
    - DNN implementation.
        - The weights of the DNN were obtained from YoloV3.
- MQTT: 
    - Communication with the ESP32.

In this algorithm we use the detection of objects using YoloV3 and OpenCV Contrib which allows the use of DNN.

<img src="https://i.ibb.co/S3Wz9Sc/process2.jpg" width="600">

In this case, I created an algorithm to calculate the approximate distance at which an object is located using YOLOV3, the algorithm is as follows.

We calculate the aperture and distance of our camera, in my case it is 19 centimeters in aperture at a distance of 16 cm.

It means that an object 19 cm wide can be at least 16 cm away from the camera so that it can fully capture it, in this case the calculation of the distance of any object becomes a problem of similar triangles.

<img src="https://i.ibb.co/cC8wbb6/esquemadist.png" width="1000">

In this case, since our model creates boxes where it encloses our detected objects, we will use that data to obtain the apparent width of the object, in this case the approximate width will be stored in a variable during the calculation.

<img src="https://i.ibb.co/jRf5xV3/exmaple.png" width="1000">

If we combine both terms we get the following equation.

<img src="https://i.ibb.co/8c8dBjB/Code-Cogs-Eqn-1.gif" width="600">

In this case for the objects that we are going to detect, we approximate the following widths in centimeters.

    {
        person:70,
        car:220,
        motorcycle:120,
        dogs:50 
    }

Here is an example of its operation with the same image.

<img src="https://i.ibb.co/wdf45wq/prockess2.jpg" width="1000">

Testing the algorithm with the camera.

<img src="https://i.ibb.co/d2dzt60/process.jpg" width="1000">
<img src="https://i.ibb.co/qjTc7rX/process1.jpg" width="1000">

Once having this distance, we will filter all distances that are greater than 2 meters, this being a safe distance to the car at the blind spot.

In turn, we will determine in which of the 2 blind spots the object is, right or left. Depending on the object and the side, the information will be sent via MQTT to the display. For example a car on the left side:

<img src="https://i.ibb.co/dMcL9gn/20200210-203839.jpg" width="600">

# The Final Product:

Product:

<img src="https://i.ibb.co/gJB4f6R/20200210-212714.jpg" width="800">
<img src="https://i.ibb.co/MZJGWgC/20200210-212619.jpg" width="800">
<img src="https://i.ibb.co/brvXxm7/20200210-212701.jpg" width="800">
<img src="https://i.ibb.co/XD4gZD9/20200210-212840.jpg" width="800">
<img src="https://i.ibb.co/LnqmYyF/20200210-212852.jpg" width="800"> 

Notifications:

<img src="https://i.ibb.co/VNWzJ37/Screenshot-20200210-212306-Messages.jpg" width="600">

### Epic DEMO:

Video: Click on the image
[![Car](https://i.ibb.co/jRBdzqS/Logo.png)](https://youtu.be/GYoLvldvk-s)

Sorry github does not allow embed videos.

# Commentary:

I would consider the product finished as we only need a little of additional touches in the industrial engineering side of things for it to be a commercial product. Well and also a bit on the Electrical engineering perhaps to use only the components we need. That being said this functions as an upgrade from a project that a couple friends and myself are developing and It was ideal for me to use as a springboard and develop the idea much more. This one has the potential of becoming a commercially available option regarding Smart cities as the transition to autonomous or even smart vehicles will take a while in most cities.

That middle ground between the Analog, primarily mechanical-based private transports to a more "Smart" vehicle is a huge opportunity as the transition will take several years and most people are not able to afford it. Thank you for reading.

## References:

Links:

(1) https://medlineplus.gov/healthysleep.html
(2) http://www.euro.who.int/__data/assets/pdf_file/0008/114101/E84683.pdf
(3) https://dmv.ny.gov/press-release/press-release-03-09-2018
(4) https://www.nhtsa.gov/risky-driving/drowsy-driving

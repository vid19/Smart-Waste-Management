import RPi.GPIO as GPIO
import time
Import random
def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(22, True)
    p.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(22, False)
    p.ChangeDutyCycle(0)

#servo motor setup
servo=22
GPIO.setup(servo,GPIO.OUT)
p=GPIO.PWM(servo,50)# 50hz frequency
p.start(0)
SetAngle(90)

#moisture sensor setup
moisture = 40
GPIO.setup(moisture, GPIO.IN)

#IR Sensor setup
ir_sensor = 38
GPIO.setup(ir_sensor, GPIO.IN)
time.sleep(2)
try:
    while True:
        a = random.randint(20,50)
        b = random.randint(20,50)
       if GPIO.input(ir_sensor):
            print("No waste placed")
        else:
            time.sleep(4)
            if GPIO.input(moisture)
                print ('No Water Detected!')
                SetAngle(45)
                time.sleep(4)
                SetAngle(90)
            else:
                print ('Water Detected!')
                SetAngle(135)
                time.sleep(4)
                SetAngle(90)
        time.sleep(0.5)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()

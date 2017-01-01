# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
#pwmPin = 18 # Broadcom pin 18 (P1 pin 12)
ledPin1 = 23 # Broadcom pin 23 (P1 pin 16)
ledPin2 = 24 # Broadcom pin 23 (P1 pin 18)
ledPin3 = 25 # Broadcom pin 23 (P1 pin 22)
#butPin = 17 # Broadcom pin 17 (P1 pin 11)

dc = 95 # duty cycle (0-100) for PWM pin

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(ledPin1, GPIO.OUT) # LED pin set as output
GPIO.setup(ledPin2, GPIO.OUT) # LED pin set as output
GPIO.setup(ledPin3, GPIO.OUT) # LED pin set as output
#GPIO.setup(pwmPin, GPIO.OUT) # PWM pin set as output
#pwm = GPIO.PWM(pwmPin, 50)  # Initialize PWM on pwmPin 100Hz frequency
#GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

# Initial state for LEDs:
GPIO.output(ledPin1, GPIO.LOW)
GPIO.output(ledPin2, GPIO.LOW)
GPIO.output(ledPin3, GPIO.LOW)
#pwm.start(dc)

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        #if GPIO.input(butPin): # button is released
          #  pwm.ChangeDutyCycle(dc)
          #  GPIO.output(ledPin, GPIO.LOW)
        #else: # button is pressed:
            #pwm.ChangeDutyCycle(100-dc)
        GPIO.output(ledPin1, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(ledPin2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(ledPin3, GPIO.HIGH)
        time.sleep(0.5)
        time.sleep(0.5)
        GPIO.output(ledPin1, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(ledPin2, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(ledPin3, GPIO.LOW)
        time.sleep(0.5)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    #pwm.stop() # stop PWM
    GPIO.cleanup() # cleanup all GPIO

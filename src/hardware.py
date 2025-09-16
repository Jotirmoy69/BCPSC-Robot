# hardware.py
import RPi.GPIO as GPIO
import time

MOTOR_LEFT = 17
MOTOR_RIGHT = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_LEFT, GPIO.OUT)
GPIO.setup(MOTOR_RIGHT, GPIO.OUT)

def move_forward(duration=1):
    GPIO.output(MOTOR_LEFT, True)
    GPIO.output(MOTOR_RIGHT, True)
    time.sleep(duration)
    GPIO.output(MOTOR_LEFT, False)
    GPIO.output(MOTOR_RIGHT, False)

def move_backward(duration=1):
    GPIO.output(MOTOR_LEFT, False)
    GPIO.output(MOTOR_RIGHT, False)
    time.sleep(duration)

def turn_left(duration=0.5):
    GPIO.output(MOTOR_LEFT, False)
    GPIO.output(MOTOR_RIGHT, True)
    time.sleep(duration)
    GPIO.output(MOTOR_LEFT, False)
    GPIO.output(MOTOR_RIGHT, False)

def turn_right(duration=0.5):
    GPIO.output(MOTOR_LEFT, True)
    GPIO.output(MOTOR_RIGHT, False)
    time.sleep(duration)
    GPIO.output(MOTOR_LEFT, False)
    GPIO.output(MOTOR_RIGHT, False)

def cleanup():
    GPIO.cleanup()

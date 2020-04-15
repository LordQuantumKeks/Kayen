# Log data from serial port
import argparse
import serial
import datetime
import time 
import os

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-d", "--device", help="device to read from", default="COM3")
parser.add_argument("-s", "--speed", help="speed in bps", default=9600, type=int)
args = parser.parse_args()

newfilename = input("What are you logging?")

outputFilePath = os.path.join('../Webseite/', newfilename + ".txt")

with serial.Serial(args.device, args.speed) as ser, open(outputFilePath, mode='wb') as outputFile:
    print("Logging started. Ctrl-C to stop.")
    time.sleep(3)
    try:
        while True:
            time.sleep(1)
            outputFile.write((datetime.datetime.now().strftime("%d.%m.%Y-%H:%M ")).encode() + (ser.read(ser.inWaiting())))
            outputFile.flush()
    except KeyboardInterrupt:
        print("Logging stopped")
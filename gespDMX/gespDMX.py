import pyudmx
import time
import sys
import keyboard
import threading
import multiprocessing
from os import system
from gespDMXlib import *

all_processes = []

#initialize gespDMX object
gD = gespDMX()

#Mainloop
while (1):
        inputtext = raw_input("gdmx> ")
        inarr = inputtext.split(" ")

        if inarr[0] == "send":
            gD.setDMX(int(inarr[1]), int(inarr[2]))
        elif inarr[0] == "chase":
            for i in range(1, 255, 1):
                gD.setDMX(int(inarr[1]), i)
                time.sleep(float(inarr[2])/1000)
        elif inarr[0] == "exit":
            system("clear")
            print("[INFO] Ciao! Bis zum naechsten Mal!")
            exit()
        elif inarr[0] == "verbose":
            gD.setVerbose(inarr[1])
        elif inarr[0] == "showError":
            gD.setShowError(inarr[1])
        elif inarr[0] == "blackout":
            gD.blackout()
        elif inarr[0] == "clear":
            system("clear")
        elif inarr[0] == "read":
            process = multiprocessing.Process(name=inarr[1],target=gD.runFile, args=[inarr[1]])
            process.start()
            all_processes.append(process)
        elif inarr[0] == "stop":
            for process in all_processes:
                process.terminate()
        else:
            print("Unbekannter Befehl!")

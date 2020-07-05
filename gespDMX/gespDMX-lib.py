import pyudmx
import time
import sys
import psutil
import keyboard
import threading
import multiprocessing
from os import system

showError = 0
all_fileProcesses = []
verbose = 0

class gespDMX:
    def __init__(self):
        system("clear")
        print("GespDMX wird gestartet.")
        sys.stdout.write("Versuche USB Interface zu laden...")
        try:
            dev = pyudmx.uDMXDevice()
            print(" Done")
        except Exception as e:
            print("Could not start uDMX interface!")
    def setDMX(self, adresse, wert):
        try:
            if verbose == 1:
                print("[DMX] Sende Wert " + str(wert) + " zur Adresse " + str(adresse))
            dev = pyudmx.uDMXDevice()
            dev.open()
            dev.send_single_value(int(adresse), int(wert))
            dev.close()
        except Exception as e:
            if showError == 1:
                print(e)
            self.setDMX(adresse, wert)
    def setVerbose(self, input):
        if input == "1":
            print("Verbose Modus ist nun AN!")
            verbose = 1
        if input == "0":
            print("Verbose Modus ist nun AUS!")
            verbose = 0
    def setShowError(self, input):
        if input == "1":
            print("Fehler werden nun angezeigt!")
            showError = 1
        if input == "0":
            print("Fehler werden nicht mehr angezeigt!")
            showError = 0
    def blackout(self):
        for i in range(0, 511):
            try:
                dev = pyudmx.uDMXDevice()
                dev.open()
                dev.send_single_value(i, 0)
                dev.close()
            except Exception as e:
                if showError == 1:
                    print(e)
    def runFile(self, name):
        while 1:
            try:
                infile = open(name + ".dmx")
                for line in infile:
                    data = line.split(' ')
                    if data[0] == "send":
                        self.setDMX(int(data[1]), int(data[2]))
                    elif data[0] == "wait":
                        if verbose == 1:
                            print("[Sleep]For " + str(int(data[1])) + " ms")
                        time.sleep(float(data[1]) / 1000)
                    else:
                        print("Komischer Befehl in Datei")
                infile.close()
            except Exception as e:
                if showError == 1:
                    print(e)
    def runFileOnce(self, name):
        try:
            infile = open(name + ".dmx")
            for line in infile:
                data = line.split(' ')
                if data[0] == "send":
                    self.setDMX(int(data[1]), int(data[2]))
                elif data[0] == "wait":
                    if verbose == 1:
                        print("[Sleep]For " + str(int(data[1])) + " ms")
                    time.sleep(float(data[1]) / 1000)
                else:
                    print("Komischer Befehl in Datei")
            infile.close()
        except Exception as e:
            if showError == 1:
                print(e)
    def runFileThread(self, name, threadname):
        process = multiprocessing.Process(name=threadname, target=self.runFile, args=[name])
        process.start()
        all_fileProcesses.append(process)
    def killFileThread(self):
        for process in all_fileProcesses:
            if process.name == "s":
                process.terminate()

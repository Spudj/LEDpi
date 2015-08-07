#!/usr/bin/pythonRoot
import RPi.GPIO as G

G.setmode(G.BCM)
G.setup(23,G.OUT)
G.output(23,True)

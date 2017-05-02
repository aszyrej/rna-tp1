#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import csv
import numpy as num
from sys import argv,exit

#Execution configurable constants
DATA_FILE='./data/tp1_ej1_training.csv'
NUM_ATTRS=10
TRAINING_DATA = []
TESTING_DATA = []
ACCEPTANCE_DATA = []

def showHelp ():
	print '''**Artificial Neural Network**
Optional parameter -d specifies data file.
Usage:
	python ej1.py -d ./data/data.csv


	'''

def splitData ():
	


def ej1 ():
	splitData()
	weights = num.random.uniform(-0.1,0.1,NUM_ATTRS)

	#NetworkBuilding
		#https://stats.stackexchange.com/questions/181/how-to-choose-the-number-of-hidden-layers-and-nodes-in-a-feedforward-neural-netw
	#Training
	for x in TRAINING_DATA:


##########################
#          MAIN          #
##########################
if __name__ == '__main__':
	
	if "-h" in argv:
		showHelp()
		exit()

	if "-d" in argv:
		DATA_FILE = argv[argv.index("-d")+1]
			
	ej1()
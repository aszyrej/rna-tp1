#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import csv
import numpy as num
from reader import *
from sys import argv,exit
from random import shuffle

#Execution configurable constants
DATA_FILE='../data/tp1_ej1_training.csv'
NUM_ATTRS=10

TRAINING_DATA_PERCENTAGE = 0.8
TESTING_DATA_PERCENTAGE = 0.1
ACCEPTANCE_PERCENTAGE = 0.1

def showHelp ():
	print '''**Artificial Neural Network**
	Optional parameter -d specifies data file.
	Usage:
	python ej1.py -d ./data/data.csv


	'''

def splitData():
	benignos, malignos = readDataEj1(DATA_FILE)
	shuffle(benignos)
	shuffle(malignos)
	training_index = int(round(len(malignos) * TRAINING_DATA_PERCENTAGE))
	testing_index = int(round(training_index + (len(malignos) * TESTING_DATA_PERCENTAGE)))
	training_data = benignos[0:training_index] + malignos[0:training_index]
	testing_data = benignos[training_index:testing_index] + malignos[training_index:testing_index]
	acceptance_data = benignos[testing_index:] + malignos[testing_index:]
	shuffle(training_data)
	shuffle(testing_data)
	shuffle(acceptance_data)
	return training_data, testing_data, acceptance_data

def ej1():
	a,b,c = splitData()
	print len(a)	
	print len(b)
	print len(c)
	weights = num.random.uniform(-0.1,0.1,NUM_ATTRS + 1)

	#NetworkBuilding
		#https://stats.stackexchange.com/questions/181/how-to-choose-the-number-of-hidden-layers-and-nodes-in-a-feedforward-neural-netw
	#Training
	#for x in TRAINING_DATA:


##########################
#          MAIN          #
##########################
if __name__ == "__main__":
	
	if "-h" in argv:
		showHelp()
		exit()

	if "-d" in argv:
		DATA_FILE = argv[argv.index("-d")+1]
	ej1()
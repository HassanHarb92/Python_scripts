#!/usr/bin/python

from __future__ import division
import sys
import math
import cmath
import numpy as np
from numpy import genfromtxt
import csv
from decimal import Decimal
import os
import random

filename1 = sys.argv[1]
filename4 = filename1.split(".")
filename3 = filename4[0]+"-data.txt"


njobs = 0
n_l9999 = 0
nline = 0
archive_start = 0
archive_end = 0
Charge = 0
Multipliticy = 0
H = 0
G = 0
EpZPE = 0

with open (filename1,'r') as input:
     for line in input:
         if "Charge =" in line:
             words = line.split()
             Charge = int(words[2])
             Multiplicity = int(words[5])
         if "Sum of electronic and zero-point Energies" in line:
             words = line.split()
             EpZPE = float(words[6])
         if "Sum of electronic and thermal Enthalpies" in line:
             words = line.split()
             H = words[6]
         if "Sum of electronic and thermal Free Energies" in line:
             words = line.split()
             G = words[7]
         if "Normal termination" in line:
             njobs = njobs + 1
         if "GINC" in line:
             n_l9999 = n_l9999 + 1
             archive_start = nline
#             print "GINC found in line ", archive_start
         if "The archive entry " in line:
             archive_end = nline 
         nline = nline + 1

nline = 0
string = ""

with open(filename1,'r') as input:
     for line in input:
         nline = nline+1
         if (nline >= (archive_start + 1)  and nline < archive_end):
            string = string + line
#            print "nline =", nline

print filename1," :  Analyzing log file . . ."
print "This file has ", njobs, " normally-terminated jobs "

lenstr = 0

with open(filename3,'w') as output:
     for i in range(0, len(string)):
         if (string[i] == "\n"):
            output.write("")
         elif (string[i] == "\\"):
            output.write("\n")
         elif ( (i +1) % 72 == 0):
            output.write("")
         elif ((i  ) % 72 == 0):
            output.write("")
         else:
            output.write(string[i])

data = np.zeros(10)
# Entries for data array:
# 0: Number of imaginary Frequencies
# 1: S^2
# 2: SCF Energy
# 3: H
# 4: G
# 5: E+ZPE
# 6: Charge
# 7: Multiplicity

data[3] = H
data[4] = G
data[5] = EpZPE
data[6] = Charge
data[7] = Multiplicity

with open (filename3,'r') as input:
     for line in input:
         if ("NImag" in line):
            words = line.split("=")
            data[0] = int(words[1])
         if ("S2=" in line):
            words = line.split("=")
            data[1] = float(words[1])
         if ("HF=" in line ):
            words = line.split("=")
            data[2] = float(words[1])

print "\n------------"
print "Job Summary"
print "------------\n"
print('{:<20s}{:>20.0f}'.format("Charge",data[6]))
print('{:<20s}{:>20.0f}'.format("Multiplicity",data[7]))
print('{:<20s}{:>20.7f}'.format("SCF Energy",data[2]))
print('{:<20s}{:>20.7f}'.format("Enthalpy",data[3]))
print('{:<20s}{:>20.7f}'.format("Free Energy",data[4]))
print('{:<20s}{:>20.7f}'.format("Electronic + ZPE",data[5]))
print('{:<20s}{:>20.0f}'.format("Imag. Freq",data[0]))
print('{:<20s}{:>20f}'.format("<S**2>",data[1]))

os.remove(filename3)


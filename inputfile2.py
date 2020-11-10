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
import csv

d1 = 17
d2 = 30
dx = 1
charge = 0
multiplicity = 7
title = "title"
commandline = "#p ub3pw91 charge stable=opt int=superfine  guess=read chkbasis"
geom1 = " O                  0.00000000    0.00000000   -1.64405400"
geom2 = " Sm                 0.00000000    0.00000000    0.21213600"

charge_geom = "0.00000000   -0.00000000 "
charge_q = "-1.0"
oldchk = "%oldchk=../../../VDEs/SmO_neutral_7_VDE.chk"
chkpt = "%chk=SmO_neutral_"

for i in range(d1,d2,dx):
    j =  i/10
    chkpt_new = chkpt+str(i)+"A.chk"
    filename = "SmO_neutral_"+str(i)+"A.com"
    with open (filename,'w') as inputfile:
         inputfile.write(oldchk)
         inputfile.write("\n")
         inputfile.write(chkpt_new)
         inputfile.write("\n")
         inputfile.write(commandline)
         inputfile.write("\n\ntitle\n\n")
         inputfile.write(str(charge))
         inputfile.write(" ")
         inputfile.write(str(multiplicity))
         inputfile.write("\n")
         inputfile.write(geom1)
         inputfile.write("\n")
         inputfile.write(geom2)
         inputfile.write("\n\n")
         inputfile.write(charge_geom)
         inputfile.write("  ")
         inputfile.write(str(j))
         inputfile.write("  ")
         inputfile.write(charge_q)
         inputfile.write("\n\n\n")



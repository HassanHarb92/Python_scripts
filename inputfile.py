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

element = sys.argv[1]

#line1_file = sys.argv[2]
#line2_file = sys.argv[3]
#line3_file = sys.argv[4]
#line4_file = sys.argv[5]
#line5_file = sys.argv[6]
#line6_file = sys.argv[7]

#line1 = open(line1_file,'r')
line1 = "#p ub3pw91 genecp scf=(novaracc,fermi,xqc) opt freq int=superfine"

#line2 = open(line2_file,'r')
line2 = "#p ub3pw91 geom=allcheck guess=read chkbasis scf=(novaracc,fermi,xqc) stable=opt int=superfine"

#line3 = open(line3_file,'r')
line3 = "#p ub3pw91 geom=allcheck guess=read chkbasis scf=(novaracc,fermi,xqc) opt freq int=superfine"

#line4 = open(line4_file,'r')
line4 = "#p ub3pw91 geom=allcheck guess=read chkbasis scf=(novaracc,fermi,xqc) stable=opt int=superfine"

#line5 = open(line5_file,'r')
line5 = "#p ub3pw91 geom=allcheck guess=read chkbasis scf=(novaracc,fermi,xqc) opt freq int=superfine"

#line6 = open(line6_file,'r')
line6 = "#p ub3pw91 geom=allcheck guess=read chkbasis scf=(novaracc,fermi,xqc) stable int=superfine"

geom1 = " O                 -0.40629098    0.97640890    0.00000000"
geom2 = "                 -1.19073710    3.19161640    0.00000000"
geom3 = "                  1.94370902    0.97640890    0.00000000"

lowspin = 1
highspin = 23

for i in range(lowspin, highspin, 2):
    filename = element+"2O_"+str(i)+".com"
    checkpoint = "%chk="+element+"2O_"+str(i)+".chk"
    print filename
    print checkpoint
    c_m = "0 "+str(i)
    with open(filename,'w') as inputfile:
         inputfile.write(checkpoint)
         inputfile.write("\n")
         inputfile.write(line1)
         inputfile.write("\n\ntitle\n\n")
         inputfile.write(c_m)
         inputfile.write("\n")
         inputfile.write(geom1)
         inputfile.write("\n")         
         inputfile.write(element)
         inputfile.write(geom2)
         inputfile.write("\n")
         inputfile.write(element)
         inputfile.write(geom3)
         inputfile.write("\n")
         inputfile.write("\nO 0\naug-cc-pvtz\n****\n@../ecp.gbs\n\n")
         inputfile.write("\n--link1--\n")
         inputfile.write(checkpoint)
         inputfile.write("\n")
         inputfile.write(line2)
         inputfile.write("\n\n\n")
         inputfile.write("\n--link1--\n")
         inputfile.write(checkpoint)
         inputfile.write("\n")
         inputfile.write(line3)
         inputfile.write("\n\n\n")
         inputfile.write("\n--link1--\n")
         inputfile.write(checkpoint)
         inputfile.write("\n")
         inputfile.write(line4)
         inputfile.write("\n\n\n")
         inputfile.write("\n--link1--\n")
         inputfile.write(checkpoint)
         inputfile.write("\n")
         inputfile.write(line5)
         inputfile.write("\n\n\n")
         inputfile.write("\n--link1--\n")
         inputfile.write(checkpoint)
         inputfile.write("\n")
         inputfile.write(line6)
         inputfile.write("\n\n\n")





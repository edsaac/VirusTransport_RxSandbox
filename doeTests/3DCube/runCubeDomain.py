###############################################################
#  _     _                        _   _      _
# | |__ (_) ___  _ __   __ _ _ __| |_(_) ___| | ___
# | '_ \| |/ _ \| '_ \ / _` | '__| __| |/ __| |/ _ \
# | |_) | | (_) | |_) | (_| | |  | |_| | (__| |  __/
# |_.__/|_|\___/| .__/ \__,_|_|   \__|_|\___|_|\___|
#               |_|
# 
###############################################################
#
# $ python3 runLeakingPoints.py [CASES.CSV] [TEMPLATE.IN]
# 
# Where:
#   - [CASES.CSV] path to csv file with the list of 
#     parameters and the corresponding tags
#   - [TEMPLATE.IN] input file template for PFLOTRAN and 
#     the corresponding tags
#   - [RUNOPTION]:
#       - debugLaptop (default)
#       - deployWorkStation
#
###############################################################

import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
from os import system
import sys

tagsCaseName =	{  
  "Title"	   	  : "<Name>"
}

## Tags dictionary for variables in input file
tagsReplaceable =	{
  ## GEOMETRY  
  "L"	      	  : "<AquiferLen>",
  "ySpan"     	: "<dummyY>",
  "H"         	: "<DomainDepth>",
  "H_1"         : "<zInBetweenLayers>",
  "r_s"	      	: "<setbackDist>",
  "r_s+l_s"   	: "<setbackPlusLeak>",
  "z_t"       	: "<wellZTop>",
  "z_b"	      	: "<wellZBottom>",
  "xyWell"	   	: "<wellXY>",
  ## MATERIALS
  ### Layer(1) | Top
  "theta1"    	: "<porosity1>",
  "k_xy1"       : "<permX1>",
  "m1"         	: "<anisotropyRatio1>",
  ### Layer(2) | Bottom
  "theta2"    	: "<porosity2>",
  "k_xy2"       : "<permX2>",
  "m2"         	: "<anisotropyRatio2>",
  ## FLOW CONDITIONS 
  "q_in"        : "<rateLeaking>",
  "Q_out"       : "<rateExtraction>",
  "C0"          : "<initialConcentration>",
  ## BIOPARTICLE
  "AttachRate"  : "<katt>",
  "DetachRate"  : "<kdet>",
  "DecayAq"     : "<decayAq>",
  "DecayIm"     : "<decayIm>",
  ## BREAKTHROUGH CURVE
  "IOdT"        : "<obsTimeStep>",
  "IOObsZ"      : "<observationAtWell>",
  ## TIMESTEPPING
  "nX"          : "<nX>",
  "nZ"          : "<nZ>",
  "deltaT"      : "<desiredTimeStep>"
}

## Path to PFLOTRAN executable
try:
  runMode = str(sys.argv[3])
except IndexError:
  print("Runmode not specified, debug assumed")
  runMode = "debugLaptop"

if "debug" in runMode:
  PFLOTRAN_path = "$PFLOTRAN_DIR/src/pflotran/pflotran "
elif "deploy" in runMode:
  PFLOTRAN_path = "mpirun -n 4 $PFLOTRAN_DIR/src/pflotran/pflotran "
else:
  print("Run mode not recognized. Defaulted to debug in laptop")
  PFLOTRAN_path = "$PFLOTRAN_DIR/src/pflotran/pflotran "

## Table with the set of parameters
try:
	parameters_file = str(sys.argv[1])
except IndexError:
	sys.exit("Parameters file not defined :(")

## Template for the PFLOTRAN input file
try:
	template_file = str(sys.argv[2])
except IndexError:
	sys.exit("Template file not found :(")

# Read CSV file with cases 
setParameters = read_csv(parameters_file)
total_rows = setParameters.shape[0]

# Check that tags in CSV are in dictionary

## Delete previous cases
system("rm -rf CASE*")

for i in range(total_rows):
  
  ## Create a folder for the case
  current_folder = "./CASE" + "{0:02}".format(i+1)
  system("mkdir " + current_folder)
  
  ## Copy template input file to folder
  fileName = setParameters.loc[i,tagsCaseName["Title"]]
  system("cp " + template_file + " " + current_folder+"/" + fileName + ".in")
  
  current_file = current_folder + "/" + fileName +".in"
 
  ## Replace tags for values in case
  for current_tag in tagsReplaceable:
    if "nX" in current_tag or "nZ" in current_tag:
      Value2Text = '{:}'.format(setParameters.loc[i,tagsReplaceable[current_tag]])
    else:
      Value2Text = '{:.3E}'.format(setParameters.loc[i,tagsReplaceable[current_tag]])
    
    COMM = "sed -i 's/" + tagsReplaceable[current_tag] + "/"\
      + Value2Text \
      + "/g' " + current_file
    system(COMM)
  
  ## Run case
  #system(PFLOTRAN_path + "-pflotranin " + current_file + " &")
  
  #sys.exit("Got Here!")
  system(PFLOTRAN_path + "-pflotranin " + current_file)
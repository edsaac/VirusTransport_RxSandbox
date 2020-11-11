import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
from os import system
import sys

FILE = str(sys.argv[1])
Cmax = 1.66E-16

try:
	CLEAN = "clean" in str(sys.argv[2])
except IndexError:
	CLEAN = False

if CLEAN:
	system("sed -i 's/,/  /g' " + FILE)
	system("head -3 " + FILE)
	system("rm -r VTK")
	system("mkdir VTK")
	system("mv *.vtk ./VTK/")
	system("rm *.out")

ObservationPoint = read_csv(FILE,sep="  ",engine="python")


Cnorm = ObservationPoint["\"Total Vaq [M] Obs__PointOutflow (100) (0.025 0.025 0.498)\""]/Cmax
Time = ObservationPoint["\"Time [d]\""]

Legend=["$\\dfrac{[V_{(aq)}]}{[V_{(aq)}]_0}$"]

fig = plt.figure(figsize=(10,4),facecolor="white")

## Plot log-scale
ax1 = plt.subplot(1,2,1)
ax1.plot(Time,Cnorm,c="black",lw=3,label=Legend[0])
ax1.set_yscale("symlog",\
 	linthresh=1.0E-6,subsy=[1,2,3,4,5,6,7,8,9])
ax1.set_ylim([-1.0E-7,1.15])
ax1.set_xlim([0,10])
ax1.set_xlabel("Time [$d$]",fontsize="large")
ax1.legend(fontsize="large")

## Plot linear-scale
ax1 = plt.subplot(1,2,2)
ax1.plot(Time,Cnorm,c="black",lw=3,label=Legend[0])
ax1.set_ylim([-1.0E-2,1.02])
ax1.set_xlim([0,10])
ax1.set_xlabel("Time [$d$]",fontsize="large")
ax1.legend(fontsize="large")

plt.savefig("./breakthrough.png",transparent=False)

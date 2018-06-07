# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:52:20 2017

@author: shysh
"""

import matplotlib.pyplot as plt
#enviroment settings
params = {'text.usetex': False, 'mathtext.fontset': 'custom'}
plt.rcParams.update(params)
plt.rc('font',family='serif')
plt.rc('font',serif='Times New Roman')
plt.figure(figsize=(12,7.5),dpi=200)
# open file to plot. the lis file must be table with only 1 detector and removed the first two lines
f1=open("copper.lis")
lines=f1.readlines()
coen=[]
cotrack=[]
for line in lines:
    content=line.split()
    judge=float(content[2])
    if (judge==0.00):
        continue
    error=float(content[3])
    if (error>90.00):
        continue
    coen.append(float(content[0])*1000)
    energy=(float(content[1])-float(content[0]))*1000
    if (energy*judge>0.000003):
        print(line)
    cotrack.append(energy*judge*4.4e18)
#plt.semilogx()
plot1=plt.plot(coen,cotrack,"y",marker="D",label="Copper")
f1.close()
plt.legend(loc="best",numpoints=1)
plt.title("Photon Spectra in Air",fontsize=23)
plt.xlabel("Energy(MeV)",fontsize=20)
plt.ylabel("Fluence($cm^{-2}$)",fontsize=20)
plt.xticks(fontsize=15,family='Times New Roman') 
plt.yticks(fontsize=15,family='Times New Roman') 
plt.show()
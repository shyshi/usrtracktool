import matplotlib.pyplot as plt
import numpy as np
import sqlite3 as sql
params = {'text.usetex': False, 'mathtext.fontset': 'custom'}
plt.rcParams.update(params)
plt.rc('font',family='serif')
plt.rc('font',serif='Times New Roman')
plt.figure(figsize=(12,7.5),dpi=200)
spfile=open("tab.lis")  # open *_tab.lis file contents spectrums
contents=spfile.readlines()
spfile.close()
detectors=0
detectorfirstline=[]
for everyline in contents:
    if everyline.startswith(" # Detector n:"):
        detectors=detectors+1
        linenumber=contents.index(everyline)
        detectorfirstline.append(linenumber)
if (detectors==0):
    print("No detectors found!")
    exit()
detectorlastline=[]
if (detectors==1):
    lines=len(contents)
    detectorlastline.append(lines)
else:
    for detector in range(0,detectors-1):
        detectorlastline.append(int(detectorfirstline[detector+1])-2)
    lines=len(contents)
    detectorlastline.append(lines)
print(detectorfirstline)
print(detectorlastline)
for detector in range(0,detectors):
    detectorfirstline[detector]=detectorfirstline[detector]+2
print(detectorfirstline)
print(detectorlastline)

conn=sql.connect("usrtrack.db")
for i in range(0,detectors):
    detectorname="detector"+str(i)
    c=conn.cursor()
    createcommand='''CREATE TABLE `'''+str(detectorname)+'''` (`Name`	TEXT,`LowEnergy`	REAL,`HighEnergy`	REAL,`EnergyRange`	REAL,`Value`	REAL,`Fluence`	REAL,`ClmuFluence`	REAL,`Error`	REAL)'''
    c.execute(createcommand)
    prefix="INSERT INTO "+str(detectorname)+" VALUES (\'" + str(detectorname)+"\',"
    subfix=")"
    clmuFluence=0.0
    for j in range(detectorfirstline[i],detectorlastline[i]):
        line=contents[j].split()
        lowenergy=float(line[0])
        highenergy=float(line[1])
        value=float(line[2])
        error=float(line[3])
        energyrange=highenergy-lowenergy
        fluence=energyrange*value
        clmuFluence=fluence+clmuFluence
        maincontent=str(lowenergy)+','+str(highenergy)+','+str(energyrange)+','+str(value)+','+str(fluence)+','+str(clmuFluence)+','+str(error)
        insertcommand=prefix+maincontent+subfix
        c.execute(insertcommand)
    conn.commit()
conn.close()
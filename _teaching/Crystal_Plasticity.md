---
title: "Crystal Plasticity 101"
collection: teaching
type: "Tutorial"
permalink: /teaching/2024-fall-teaching-4
excerpt: ""
venue: "by Prof. Zhang"
date: 2024-10-16
location: "Beijing, China"
---
# Rate Dependent Crystal Plasticity Model
Crystal plasticity finite element method (CPFEM) is a powerful tool in the field of mechanics and materials sciences.
It enables the simulation and analysis of the mechanical behavior of crystalline materials at the micro - and meso - scales.

Usually, the crystal plasticity model is implemented in commercial finite element software through a user subroutine UMAT/VUMAT. 
In Abaqus, users can write subroutines in Fortran programming languages to define the constitutive behaviors based on crystal plasticity theories. 
Basic equations and VUMAT user subroutine for Abaqus/Explicit can be found at <a href='https://github.com/yzhang951/CPFEM-VUMAT/tree/main/Base' target="_blank">https://github.com/yzhang951/CPFEM-VUMAT/tree/main/Base</a>.

We decide to use Explicit and VUMAT, because it does not require complex tangent modulus calculations, making it simple for fast model development. 

## Step 1: Download
Download CPFEM VUMAT user subroutine from GitHub. 
```bash
git clone https://github.com/yzhang951/CPFEM-VUMAT.git
cd CPFEM-VUMAT/Base
```
The **vumat.for** is the main VUMAT Fortran file, **Job-1.inp** is the input file for Abaqus, and **aeuler** is the Euler angles for each element.

## Step 2: Modify Abaqus .inp file
If you are familiar with Abaqus, the input file should be pretty self-explanatory. 
You can tweak some parameters in **Job-1.inp**, such as material properties, strain rate, loading scheme, etc..
```
*User Material, type=MECHANICAL, constants=18
204.6E3, 137.7E3 , 126.2E3, 45.0, 90.0, 0.0, 0.001 , 0.02,
50.0   , 1000.0  , 70.0   , 4.0 , 1.0 , 1.4, 60.0E3, 1.0E3,
4.0E3  , 100.0
```
The meaning of these material properties can be found at **Assign props() array to logical variable names** section in **vumat.for**.

Another important quantity is the density here, as we are using mass scaling to boost the simulation speed. 
The simulation timestep would be determined by the density \\(\rho\\) through \\(\Delta t\propto \Delta x\sqrt{\rho /E}\\), where *E* is the Young's modulus.

## Step 3: Modify **vumat.for** file
Two important parameters to change in the **vumat.for** are **num_ele** and **FILE1**.The first one is the number of elements in the simulations, if you change the mesh in the input file please modify this one accordingly. 
The other one **FILE1** is the path of Euler angle file. Both absolute or relative path would be fine here.

### Caution
There are two **num_ele** in the code, one on line 44 and another on line 114.

The code is designed for single crystal and polycrystals, therefore there are two ways to read in the Euler angles at line 247.
```
c--------------- Read in Euler angles from external file ------------
c--- Important!: comment this section for poly xtal simulations -----
c--- the Euler angles will be read from file 'aeuler' through VUSDFLD
           psi_t(1) = psi_ang*PI/180.0
           psi_t(2) = theta_ang*PI/180.0
           psi_t(3) = phi_ang*PI/180.0
```

## Step 4: Run simulation
You can execute the **run.sh** to start the simulations. The double precision is mandatory here to keep the consistence as we use **real*8** in **vumat.for**.
```bash
tail -f Job-1.sta
```
This command could be used to monitor the simulation process.

## Step 5: Postprocessing
Python interface is very useful to postprocess the Abaqus output. Here is an example I used to extract elastic lattice strain for DP-HEA project.
The script cannot be used directly here due to different defination of Set and number of elements. Please modify accordingly.
```python
from odbAccess import *
import numpy as np
import math as mt

#Reading output database
odbpath = 'J_8000.odb'
odb = openOdb(path=odbpath)
assembly = odb.rootAssembly

print 'Model data for ODB: ', odbpath

#Reading history output data
step = odb.steps['Step-1']
Node_Start = 1
Node_End = 9241

U = np.zeros(201)
F = np.zeros(201)

for i in range(Node_Start,Node_End+21,21):
    node = 'Node PART-1-1.' + str(i)
    region = step.historyRegions[node]
    u1data = region.historyOutputs['U2'].data
    f1data = region.historyOutputs['RF2'].data
    j = 0
    for time,force in f1data:
        F[j] = F[j] + force
        j = j + 1

j = 0
for time,disp in u1data:
    U[j] = disp      
    j = j + 1

dispFile = open('fitting.dat','w')

for i in range(len(U)):
    j = i 
    dispFile.write("%10.4E  %10.4E\n" % ((U[j]/20)*100,F[j]/1E6/400*(1+U[j]/20)))
dispFile.close()
#######################################################################
#######################################################################
#######                                                         #######
#######            Lattice strain calculations!                 #######
#######                                                         #######
#######################################################################
#######################################################################
print('\nExtracting lattice strain along LD')

LD = []
LD.append(assembly.elementSets['FCC-LD200'])
LD.append(assembly.elementSets['FCC-LD220'])
LD.append(assembly.elementSets['FCC-LD111'])
LD.append(assembly.elementSets['FCC-LD311'])
LD.append(assembly.elementSets['FCC-LD331'])
LD.append(assembly.elementSets['BCC-LD200'])
LD.append(assembly.elementSets['BCC-LD110'])
LD.append(assembly.elementSets['BCC-LD211'])
LD.append(assembly.elementSets['BCC-LD321'])

fp = open('lattice_strain_LD.dat','w')
for i in odb.steps['Step-1'].frames:
#    print('\nExtracting from Frame:\t'+str(i.frameId))
    # calculate the average stress
    stress = 0.0
    x = i.fieldOutputs['S'].values
    for j in x:
        stress = stress + j.data[1]
    stress = stress/len(x)/1E6
    fp.write("%10.4E  " % stress)
    for j in LD:
        temp = 0.0
        field = i.fieldOutputs['SDV5'].getSubset(region=j).values
        for k in field:
            temp = temp + k.data
        temp = temp/len(field)
        fp.write("%10.6E  " % temp)
    fp.write("\n")

    tempF = 0.0
    numF = 0
    tempB = 0.0
    numB = 0
    for j in LD[0:4]:
        field = i.fieldOutputs['S'].getSubset(region=j).values
        for k in field:
            tempF = tempF + k.data[1]
            numF = numF + 1
    for j in LD[5:8]:
        field = i.fieldOutputs['S'].getSubset(region=j).values
        for k in field:
            tempB = tempB + k.data[1]
            numB = numB + 1
    print("%10.3f  %10.3f" % (tempF/numF/1E6,tempB/numB/1E6)) 

fp.close()


#print('\nExtracting lattice strain along TD')

TD = []
TD.append(assembly.elementSets['FCC-TD200'])
TD.append(assembly.elementSets['FCC-TD220'])
TD.append(assembly.elementSets['FCC-TD111'])
TD.append(assembly.elementSets['FCC-TD311'])
TD.append(assembly.elementSets['FCC-TD331'])
TD.append(assembly.elementSets['BCC-TD200'])
TD.append(assembly.elementSets['BCC-TD110'])
TD.append(assembly.elementSets['BCC-TD211'])
TD.append(assembly.elementSets['BCC-TD321'])

fp = open('lattice_strain_TD.dat','w')
for i in odb.steps['Step-1'].frames:
#    print('\nExtracting from Frame:\t'+str(i.frameId))
    # calculate the average stress
    stress = 0.0
    x = i.fieldOutputs['S'].values
    for j in x:
        stress = stress + j.data[1]
    stress = stress/len(x)/1E6
    fp.write("%10.4E  " % stress)
    for j in TD:
        temp = 0.0
        field = i.fieldOutputs['SDV4'].getSubset(region=j).values
        for k in field:
            temp = temp + k.data
        temp = temp/len(field)
        fp.write("%10.6E  " % temp)

    fp.write("\n")

fp.close()
```

### Reference of Crystal Plasticity Model
"Overview no. 42 texture development and strain hardening in rate dependent polycrystals." **Acta Metall**. 33, 923–953, (1985).

"Crystallographic texture evolution in bulk deformation processing of FCC metals. " **Journal of the Mechanics and Physics of Solids**, 40, 537–569 (1992).

### Our recent paper using CPFEM

"Additively manufactured hierarchical stainless steels with high strength and ductility." **Nature Materials**, 17, 63-71 (2018)

"Microscale residual stresses in additively manufactured stainless steel." **Nature Communications**, 10, 4338 (2019).

"Modeling of microscale internal stresses in additively manufactured stainless steel." **Modelling and Simulation in Materials Science and Engineering**, 30, 074001 (2022).

"Strong yet ductile nanolamellar high-entropy alloys by additive manufacturing." **Nature**, 608, 62-68 (2022)

"Modeling of crack tip fields and fatigue crack growth in fcc crystals." **Journal of the Mechanics and Physics of Solids**, 188, 105691 (2024)

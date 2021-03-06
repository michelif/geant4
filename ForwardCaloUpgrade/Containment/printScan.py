#!/usr/bin/python

import math


# first print the lyso line
print "./runEEShashlik -m run20GeV.mac -actType LYSO -n 28 -act 1.5 -abs 2.5"
print "mv EEShash.root EEShash_LYSO.root"


# then start the scan for the cef3
# the scan will keep the cef3 thickness fixed to 5mm
# and scan all possible tungsten thicknesses


X0_tung = 3.5 # in mm
X0_cef3 = 16.8 # in mm

X0_target = 24.

detectorLength = 0.

cef3_thickness = 5. # in mm, fixed

tung_thickness = 0.


while tung_thickness<8. :

  tung_thickness += 0.5 

  X0_tung_singleLayer = tung_thickness/X0_tung
  X0_cef3_singleLayer = cef3_thickness/X0_cef3

  nLayers = math.ceil( X0_target / (X0_tung_singleLayer+X0_cef3_singleLayer) )
  X0_eff = nLayers*X0_cef3_singleLayer + nLayers*X0_tung_singleLayer
  detectorLength = nLayers*cef3_thickness + nLayers*tung_thickness

  if detectorLength>225.: continue # actually should be 220, but there's a configuration of 221mm so i want to check it

  print "./runEEShashlik -m run20GeV.mac -actType CeF3 -n " + str(int(nLayers)) + " -act " + str(cef3_thickness) + " -abs " + str(tung_thickness) 
  print "mv EEShash.root EEShash_CeF3_tung" + str(int(10.*tung_thickness)) + "_nLayers" + str(int(nLayers)) + ".root"

  

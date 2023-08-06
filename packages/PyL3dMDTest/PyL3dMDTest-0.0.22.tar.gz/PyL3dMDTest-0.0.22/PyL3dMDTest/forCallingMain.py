# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 18:50:12 2022

@author: pawan
"""
from main import PyL3dMD


if __name__ == "__main__":
    datafilename =  'methylpentaneAA.txt'
    dumpfilename = 'NPT_w_methylpentaneAA_T100CP1atm.lammpstrj'
    SetFromFrame = 0
    SetToFrame = 1
    SetFrameInterval = 1
    dumpfilename = 'NPT_w_methylpentaneAA_T100CP1atm.lammpstrj'
    program = PyL3dMD(datafilename, dumpfilename, FromFrame=SetFromFrame, ToFrame=SetToFrame, FrameInterval=SetFrameInterval, numberofcores=4)
    program.start()

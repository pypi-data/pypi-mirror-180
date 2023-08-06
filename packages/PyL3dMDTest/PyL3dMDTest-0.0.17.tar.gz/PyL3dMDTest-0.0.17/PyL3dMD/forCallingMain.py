# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 18:50:12 2022

@author: pawan
"""
from PyL3dMD import PyL3dMD


if __name__ == "__main__":
    locationDataFile = ""
    locationDumpFile = ""
    datafilename = 'methylpentaneAA.txt'
    dumpfilename = 'NPT_w_methylpentaneAA_T100CP1atm.lammpstrj'
    program = PyL3dMD(datafilename, dumpfilename, numberofcores=4)
    program.start()

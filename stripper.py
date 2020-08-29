# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:45:22 2020
@author: Sheikh Ahnaf Alvi
"""
import re
import numpy as np
import os
import sys

#load the twister file

cwd=os.getcwd()
print(cwd)
file=sys.argv[1]
out="lammps_"+file[:-4]+".txt"
print(os.path.join(cwd,file))

    
with open(file,"r") as f:
     lines=f.readlines()
    
      
for line in lines:
   with open(out,"a") as fo:
        fo.writelines(re.sub('\s+',' ',line)+"\n")
     
   print(re.sub('\s+',' ',line))
   
   
        
        
        

        
        

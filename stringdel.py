import re

file=input('filename')
with open(file,'r') as f:
     lines=f.readlines()
for line in lines:
  listline=line.split(" ")
  for l in listline:
      print(l[0])
      if l[0]=='ITEM:':
      	 flag=1
      	 
      else:
         flag=0	 
  with open('dmd.dat','a') as g:
       #g.writelines(re.sub('','',line)) 
        if flag:
      	   g.writelines('')
        else:
           g.writelines(line)

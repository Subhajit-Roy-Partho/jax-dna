#!/usr/bin/env python27
import math
import sys,os

def is_symmetric(seq):
  symmetric_points = 0
  for i in range(length):
   	if (seq[i] == 'A' and seq[length - 1 -i] == 'T') or  (seq[i] == 'C' and seq[length - 1 -i] == 'G') or  (seq[i] == 'G' and seq[length - 1 -i] == 'C')  or (seq[i] == 'T' and seq[length - 1 -i] == 'A'):
            symmetric_points += 1

  symmetric = 0

  if(symmetric_points == len(seq)):
        symmetric = 1
  
  return symmetric 



def get_TM(seq,boxsize=20,salt_conc=0.5):
  length = len(seq);
  deltaH = 0;
  deltaS = 0;
  molarconcentration = 2.6868994 / (boxsize*boxsize*boxsize) ;
 
  symmetric_points = 0
  for i in range(length):
   	if (seq[i] == 'A' and seq[length - 1 -i] == 'T') or  (seq[i] == 'C' and seq[length - 1 -i] == 'G') or  (seq[i] == 'G' and seq[length - 1 -i] == 'C')  or (seq[i] == 'T' and seq[length - 1 -i] == 'A'):
            symmetric_points += 1

  symmetric = 0

  if(symmetric_points == len(seq)):
        symmetric = 1
  
  for  i in range (length-1) :
        
     pair = seq[i] + seq[i+1];

     if(pair ==  "AA" ):  
	 deltaH += -7.6 
	 deltaS += -21.3; 
     if (pair == "TT"):
	 deltaH += -7.6
	 deltaS += -21.3; 

     if (pair == "TA"):
	 deltaH += -7.2
	 deltaS += -20.4
      
     if (pair == "AT"):
	 deltaH += -7.2
	 deltaS += -21.3
      
     if (pair == "AC"):
	 deltaH += -8.5
	 deltaS += -22.7

     if (pair == "GT"):
	 deltaH += -8.5
	 deltaS += -22.7
      
     if (pair == "TG"):
	deltaH += -8.4
	deltaS += -22.4; 

     if (pair == "CA"):
	 deltaH += -8.4
	 deltaS += -22.4; 
        

     if (pair == "TC"):
	 deltaH += -7.8
	 deltaS += -21.0; 

     if (pair == "GA"):
	 deltaH += -7.8
	 deltaS += -21.0; 
      
     if (pair == "AG"):
 	 deltaH += -8.2;
 	 deltaS += -22.2; 

     if (pair == "CT"):
	 deltaH += -8.2
	 deltaS += -22.2; 
      
 
     if (pair == "GC"):
	 deltaH += -10.6
	 deltaS +=  -27.2; 
      
     if (pair == "CG"):
	 deltaH += -9.8
	 deltaS += -24.4;

     if (pair == "GG"):
	 deltaH += -8.0;
	 deltaS += -19.9; 

     if (pair == "CC"):
	 deltaH += -8.0;
	 deltaS += -19.9; 
       
      
  
    
    
  if(seq[0] == 'A' or seq[0] == 'T'):
   	deltaH += 2.2;
	deltaS += 6.9;
   



  if(seq[length-1] == 'A' or seq[length-1] == 'T'):
	deltaH += 2.2;
	deltaS += 6.9;
   

  deltaH += 0.2;
  deltaS += -5.7;

  deltaH *= 1000.0;

  divisor = 2.0;
 
  if(symmetric):
     deltaS += -1.4;
     divisor = 0.5;

  salt_correction = 0.368 * (len(seq) - 1.0)  * math.log(salt_conc)
  deltaS += salt_correction

 
  GAS_CONSTANT =  1.9858775 


  Tm = deltaH / (deltaS + GAS_CONSTANT * math.log(molarconcentration/divisor) );
  return Tm - 273.15 



if len(sys.argv) != 2:
	print "Usage: ./gensek <length> "
	sys.exit(1)
 
length = int(sys.argv[1])

import random
import time

seed = int(time.time())


random.seed(seed)


bases = ['A','C','G','T']

#print get_TM('CAGGTCG',20,1.0)
#print get_TM('TAGAAATGCAAG',20,0.5)

#sys.exit(1)

minT = 500
maxT = 0

genseqs = []
gentemps = []

import itertools

for it in itertools.product('ACGT',repeat=length):
	sek =  ''.join(it)
	temp = get_TM(sek)
	if not is_symmetric(sek):
		if temp > maxT:
			maxT = temp
		if temp < minT:
			minT = temp
		genseqs.append(sek)
		gentemps.append(temp) 

import numpy as np
import sys

avgtemp = np.array(gentemps).mean()



for i in range(len(genseqs)):
        print genseqs[i] 
	if gentemps[i] < 0:
		print >> sys.stderr, 'Warning, sequence ', genseqs[i], ' has temeperature ', gentemps[i]


print >> sys.stderr, 'Max temp:', maxT, ' min temp:', minT, 'avg temp: ', avgtemp



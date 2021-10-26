import os
import sys
import pandas as pd
import numpy as np


carDf=pd.read_csv('./files/cars.csv',sep=",",header=0)
autoDf=pd.read_csv('./files/auto-mpg.csv',sep=",")


print (os.environ.get('PYHTONPATH','Not There'))

print (os.getcwd())
print(' hello ')
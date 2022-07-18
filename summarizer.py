import sys
import pandas as pd

arguments = len(sys.argv)-1
print(arguments)

if(arguments == 1):
    csv= sys.argv[1]
    data=pd.read_csv(csv)

    print(data.dtypes)
else:
    print("python summarizer.py data.csv")

    
#import csv

#with open('data.csv') as File:
#    reader = csv.reader(File, delimiter=',', quotechar=',',
#                        quoting=csv.QUOTE_MINIMAL)
    


    
#    for row in reader:
#         for x in row:
#            print(x)
#             print(type(x))
#             try:
#                 print(int(x))
#             except:
#                 print("No es int")
#             if isinstance(x,int):
#                 print(x)
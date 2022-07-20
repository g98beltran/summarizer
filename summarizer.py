import sys
import pandas as pd

arguments = len(sys.argv)-1
#print(arguments)

if(arguments == 1):
    csv= sys.argv[1]
    data=pd.read_csv(csv)

    colum_names=data.columns.values
    #print(colum_names)

    columNumeric = []
    #print(data.dtypes)
    #print(len(colum_names))
    #print(colum_names[1])
    #print(data[""+colum_names[3]].dtype)
    #print(len(colum_names)-1)
    
    ignored_colums=[]
    
    i = 0

    while i <= len(colum_names)-1:
        
        colum_type = data[""+colum_names[i]].dtype
       
        #print(data[colum_names[i]].dtype)
        if colum_type != "object" :
            columNumeric.append(colum_names[i])
        else:
            ignored_colums.append(colum_names[i])
        
        i = i +1

    print("- Analyzed "+str(csv))
    print("- Found "+str(len(colum_names))+" columns")
    print("- Found "+str(len(data))+" rows")
    print("- Generating stats...")
    notnumeric = ""
    for c in ignored_colums:
        notnumeric += str(c)+" "
    
    print("- Ignoring colums "+notnumeric+" because are not of type numeric")

    print("\nStats:\n")
    for x in columNumeric:
        print("-Colum "+x+"\n")
        print("\t -min value "+str(min(data[""+x])))
        print("\t -max value "+str(max(data[""+x])))
        print("\t -average value "+str(data[""+x].mean()))
        print("\t -std value "+str(data[""+x].std()))
    
    #print(columNumeric)
    #print(data["date"].dtype)
    #print(data["date"])
    
    #print(min(data["date"]))
    #print(max(data["date"]))
    #print(data["date"].mean())
    #print(data["date"].std())
    
    #for fechas in data["date"] :
        


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
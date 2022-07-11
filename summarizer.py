import csv

with open('data.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        for x in row:
            print(x)
            print(type(x))
            try:
                print(int(x))
            except:
                print("No es int")
            if isinstance(x,int):
                print(x)

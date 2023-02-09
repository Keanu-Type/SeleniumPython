import csv
import pandas as pd
x = int(1)
y = int(0)

with open("Units_Alchemist_Code.csv",'r+') as csv_file:
    
    units = csv.reader(csv_file)
    next(units)
    df=pd.read_csv("Units_Alchemist_Code.csv")
    #pd
    #change = list(units)
    for line in units:
        x=x+1
        if(line[3]=="True"):
            print(line[1], end=" ")
            print(line[2], end=" ")
            print(line[3], end=" ")
            print(x)
        #elif(line[3]=="False"):
        #    df.head(1)
        #    df._set_value(x, "STATUS", "True")
            #df.loc[df["STATUS"]=="False", "STATUS"] = "True"
        #    df.to_csv("Units_Alchemist_Code.csv",index=False)
       #x=x+1
            


import csv

def read_data(filename):
    with open(filename,"r") as csvfile:
        datareader=csv.reader(csvfile,delimiter=",")
        traindata=[]
        for row in datareader:
            traindata.append(row)
    return traindata

def findS():
    data=read_data("ENJOYSPORT.csv")
    rows=len(data)
    columns=len(data[0])-1
    h=['0']*columns
    for i in range(1,rows):
        print(data[i])
        if data[i][columns]=='1':
            for j in range(columns):
                if data[i][j]==h[j]:
                    pass
                elif data[i][j]!=h[j] and h[j]=='0':
                    h[j]=data[i][j]
                elif data[i][j]!=h[j] and h[j]!='0':
                    h[j]='?'
    print("\nMaximally Specific Hypothesis for the dataset is \n")
    print("<",end=" ")
    for j in range(len(h)):
        print(h[j],",",end=" ")
    print(">",end=" ")
findS()


            
        
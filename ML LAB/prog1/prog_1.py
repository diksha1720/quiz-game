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
            for j in range(0,columns):
                if h[j]==data[i][j]:
                    pass
                elif h[j]!=data[i][j] and h[j]=='0':
                    h[j]=data[i][j]
                elif h[j]!=data[i][j] and h[j]!='0':
                    h[j]='?'
    print("Maximally specific hypothesis is :")
    print("<",end=" ")
    for j in range(len(h)):
        print(h[j],end=", ")
    print(">",end=" ")
findS()
import csv

def read_data(filename):
    with open(filename,"r") as csvfile:
        datareader=csv.reader(csvfile,delimiter=",")
        traindata=[]
        for row in datareader:
            traindata.append(row)
    return traindata

a=read_data('ENJOYSPORT.csv')
rows=len(a)
columns=len(a[0])-1

print("Initial values for Hypotheses\n")
S=['0']*columns
G=['?']*columns
print('S0  ',S)
print('G0  ',G)

for j in range(columns):
    S[j]=a[0][j]
    
temp=[]   
 
for i in range(rows):
    print("\n..............................................................\n")
    if a[i][columns]=="Yes":
        for j in range(columns):
            if a[i][j]!=S[j]:
                S[j]='?'
        for j in range(columns):
            for k in range(1,len(temp)):
                if temp[k][j]!=S[j] and temp[k][j]!='?':
                    del(temp[k])
        print("for example{0} the hypothesis is S{0} ".format(i+1),S)
        if(len(temp)==0):
            print("for example{0} the hypothesis is G{0} ".format(i+1),G)
        else:
            print("for example{0} the hypothesis is G{0} ".format(i+1),temp)
    if a[i][columns]=="No":
        for j in range(columns):
            if a[i][j]!=S[j] and S[j]!='?':
                G[j]=S[j]
                temp.append(G)
                G=['?']*columns
        print("for example{0} the hypothesis is S{0} ".format(i+1),S)
        print("for example{0} the hypothesis is G{0} ".format(i+1),temp)

        
        
            
    

        
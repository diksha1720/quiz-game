
# import csv
# a = []
# print("\n The Given Training Data Set \n")

# with open("ENJOYSPORT.csv", "r") as csvFile:
#     reader = csv.reader(csvFile)
#     for row in reader:
#         a.append(row)
#         print(row)
# num_attributes = len(a[0]) - 1

# print("\n The initial value of hypothesis: ")
# S = ["0"] * num_attributes
# G = ["?"] * num_attributes
# print("\n The most specific hypothesis S0 : [0,0,0,0,0,0]\n")
# print(" \n The most general hypothesis G0 : [?,?,?,?,?,?]\n")

# # Comparing with First Training Example
# for j in range(0, num_attributes):
#     S[j] = a[0][j]

# # Comparing with Remaining Training Examples of Given Data Set

# print("\n Candidate Elimination algorithm  Hypotheses Version Space Computation\n")
# temp = []
# for i in range(0, len(a)):
#     print("------------------------------------------------------------------------------")
#     if a[i][num_attributes] == "Yes":
#         for j in range(0, num_attributes):
#             if a[i][j] != S[j]:
#                 S[j] = "?"

#         for j in range(0, num_attributes):
#             for k in range(1, len(temp)):
#                 if temp[k][j] != "?" and temp[k][j] != S[j]:
#                     del temp[k]

#         print(" For Training Example No :{0} the hypothesis is S{0}  ".format(i + 1), S)
#         if len(temp) == 0:
#             print(" For Training Example No :{0} the hypothesis is G{0} ".format(i + 1), G)
#         else:
#             print(" For Training Example No :{0} the hypothesis is G{0}".format(i + 1), temp)

#     if a[i][num_attributes] == "No":
#         for j in range(0, num_attributes):
#             if S[j] != a[i][j] and S[j] != "?":
#                 G[j] = S[j]
#                 temp.append(G)
#                 G = ["?"] * num_attributes

#         print(" For Training Example No :{0} the hypothesis is S{0} ".format(i + 1), S)
#         print(" For Training Example No :{0} the hypothesis is G{0}".format(i + 1), temp)

import csv

a=[]
print('The given dataset\n')
with open('ENJOYSPORT.CSV','r') as csvfile:
    datareader=csv.reader(csvfile, delimiter=',')
    for row in datareader:
        a.append(row)
        print(row)

num_attributes=len(a[0])-1

print("The values of Hypotheses initially\n")
S=["0"]*num_attributes
G=["?"]*num_attributes
print("Most specific hypothesis is S0: ['0','0','0','0','0','0']\n")
print("Most general hypothesis is S0: ['?','?','?','?','?','?']\n")

for j in range(0, num_attributes):
    S[j]=a[0][j]


temp=[]
print("Computing the Candidate Elimination Hypothesis version space\n")
for i in range(0, len(a)):
    print("\n......................................................................\n")
    if a[i][num_attributes]=='Yes':
        for j in range(0,num_attributes):
            if S[j]!=a[i][j]:
                S[j]='?'

        for j in range(0,num_attributes):
            for k in range(1,len(temp)):
                if temp[k][j]!=S[j] and temp[k][j]!='?':
                    del temp[k]

        print("For example{0} the most specific hypothesis is S{0} ".format (i+1),S)
        if len(temp)==0:
            print("For example{0} the most general hypothesis is G{0} ".format (i+1),G)
        else:
            print("For example{0} the most general hypothesis is G{0} ".format (i+1),temp)

    if a[i][num_attributes]=='No':
        for j in range(0,num_attributes):
            if S[j]!=a[i][j] and S[j]!='?':
                G[j]=S[j]
                temp.append(G)
                G=['?']*num_attributes
        print("\nFor example{0} the most specific hypothesis is S{0} \n".format (i+1),S)
        print("\nFor example{0} the most general hypothesis is G{0} \n".format (i+1),temp)
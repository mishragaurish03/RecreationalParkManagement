from apyori import apriori
import pandas as pd
import matplotlib.pyplot as plt

#read data to the dataframe
df = pd.read_csv('test.csv')
#Generating list of choices
trn = []
for i in range(len(df)):
    temp = []
    for j in range(3,11):
        if df.values[i,j]==1:
            temp.append(df.columns[j])
    if len(temp)>2:
        trn.append(temp)

#Extracting the assosiation rules
rules= apriori(transactions= trn, min_support=0.003, min_confidence = 0.3, min_lift=3, min_length=3)  
results= list(rules)  

#Output the Assosiation Rules
for item in results:
    #first index of list contains frequent item set
    print("Frequest Item Set====================")
    pair = item[0] 
    items = [x for x in pair]
    print(items)

    #second index of the inner list contains support
    print("Support: " + str(item[1]))

    #third index of the list contains assosiation rule
    for i in item[2]:
        print("Rule: " + str([x for x in i[0]]) + " -> " + str([x for x in i[1]]))
        print("Confidence: " + str(i[2]))
        print("Lift: " + str(i[3]))
        print("=====================================")

#Plotting the confidence and Lift

#LHS=[]
#RHS=[]
CONF=[]
LIFT=[]

for item in results:
    for i in item[2]:
        CONF.append(i[2])
        LIFT.append(i[3])
        #temp=[x for x in i[0]]
        #LHS.append(temp)
        #temp=[x for x in i[1]]
        #RHS.append(temp)

n=[i for i in range(len(CONF))]
plt.scatter(CONF,LIFT,c=n)

for i, txt in enumerate(n):
    plt.annotate(txt, (CONF[i], LIFT[i]))
plt.show()


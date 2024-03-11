import csv
import numpy as np
from scipy.stats import chisquare
import matplotlib.pyplot as plt


candidate_key = {1:'Taimur Saleem Khan',2:'Jalal Khan',3:'Muhammad Sadeeq'}
ecl = [0,0]
pti = [0,0]
i=1
with open('PK-79-Unofficial.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count >0:
            pti[0]+=float(row[1])
            pti[1]+=float(row[2])
            
        line_count += 1

i=1
with open('PK-79-official.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count >0:
            ecl[0]+=float(row[1])
            ecl[1]+=float(row[2])
                    
        line_count += 1


import numpy as np  
import matplotlib.pyplot as plt  
from scipy.spatial import distance

print('taimur',ecl[0]-pti[0])
print('jalal',ecl[1]-pti[1])
keys = [0,1]
keys.sort()
plt.figure()
x = []
y_ecl = []
y_pti = []
for i in keys:
    x.append(i)
    y_ecl.append(ecl[i])
    y_pti.append(pti[i])

x = np.arange(len(x)) 


plt.bar(x - 0.2, y_ecl, 0.4, label = 'Jalal Khan', color='#00401A') 
plt.bar(x + 0.2, y_pti, 0.4, label = 'Taimur Jhagra', color='#ff0000') 


plt.ylim(0, max(max(y_ecl),max(y_pti))+0.25*max(max(y_ecl),max(y_pti)))

plt.xlabel('Form Types', fontsize=24)
plt.ylabel('Votes', fontsize=30)
#plt.title('Total Votes of Each Candidate on the different Forms', fontsize=24)
plt.xticks(x, ['ECL', 'PTI'], fontsize=24)

plt.legend(fontsize=24) 

#plt.xticks(fontsize=16)
plt.yticks(fontsize=24)

#ax.set_xticks(labels[::4])

figure = plt.gcf()  # get current figure
figure.set_size_inches(18, 9)
# Crop tight (using bbox_inches='tight')
plt.savefig("Votes_Lost.png", bbox_inches='tight')  # Replace "plot.png" with your desired filename

#plt.bar(x, y, color='#E81B23') 

#plt.bar(x, y, color='#00AEF3') 




import csv
import numpy as np
from scipy.stats import chisquare
import matplotlib.pyplot as plt


candidate_key = {1:'Taimur Saleem Khan',2:'Jalal Khan',3:'Muhammad Sadeeq'}
ecl = {}
pti = {}
i=1
with open('PK-79-Unofficial.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count >0:
            for i in range(1,3):
                cand = candidate_key[i]
                if cand not in pti:
                    pti[cand] = []
                pti[cand].append(float(row[i]))
            
            
        line_count += 1

i=1
with open('PK-79-official.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count >0:
            for i in range(1,3):
                cand = candidate_key[i]
                if cand not in ecl:
                    ecl[cand] = []
                ecl[cand].append(float(row[i]))
                    
        line_count += 1

diff = {}
for cand in ecl:
    if cand not in diff:
        diff[cand] = []
    for i in range(0,len(ecl[cand])):
        diff[cand].append(ecl[cand][i]-pti[cand][i])



import numpy as np  
import matplotlib.pyplot as plt  
from scipy.spatial import distance
x = np.array(list(range(1,len(ecl[cand])+1)))

# Plotting stems

# Plotting horizontal stems using hlines()
plt.hlines(x, 0, diff['Taimur Saleem Khan'], linestyles='--', colors='r', label='Taimur Jhagra')
plt.hlines(x, 0, diff['Jalal Khan'], linestyles='--', colors='g', label='Jalal Khan')

# Plotting markers for stem ends
plt.plot(diff['Taimur Saleem Khan'], x, 'ro')
plt.plot(diff['Jalal Khan'], x, 'go')

# Plot the baseline for the stems
plt.plot([0, 0], [x.min(), x.max()], 'k-')

# Add labels, ticks, and legend
plt.xlabel('← More Votes in PTI Form | More Votes in ECL Form →', fontsize=24)
plt.ylabel('Polling Station', fontsize=24)
plt.legend(fontsize=16)
plt.yticks(x, fontsize=12)
plt.xticks(fontsize=18)
plt.xlim(-900, 900)
figure = plt.gcf()  # get current figure
figure.set_size_inches(9, 18)
plt.gca().invert_yaxis()  # Invert y-axis for better readability

# Crop tight (using bbox_inches='tight')
plt.savefig("polling_station_difference.png", bbox_inches='tight')  # Replace "plot.png" with your desired filename

#plt.bar(x, y, color='#E81B23') 

#plt.bar(x, y, color='#00AEF3') 




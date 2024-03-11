import csv
import numpy as np
from scipy.stats import chisquare
import matplotlib.pyplot as plt


D = []
R = []
i=1
with open('precient_freq.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
    
        if line_count ==0:
            for i in range(1,len(row)):
                R.append(float(row[i]))
        else:
            for i in range(1,len(row)):
                D.append(float(row[i]))
        
        line_count += 1



x = list(range(0,10))
y = []
for i in D:
    y.append(i/sum(D))

plt.axhline(y=0.1, color='gray', linestyle='--')

plt.bar(x, y, color='#00AEF3') 
plt.ylim(0, 0.15)

plt.xlabel('Unit Digit', fontsize=24)
plt.ylabel('Proportion', fontsize=24)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

#ax.set_xticks(labels[::4])

figure = plt.gcf()  # get current figure
figure.set_size_inches(18, 9)
# Crop tight (using bbox_inches='tight')
plt.savefig("US_election_2022_Biden.png", bbox_inches='tight')  # Replace "plot.png" with your desired filename

x = list(range(0,10))
y = []
for i in R:
    y.append(i/sum(R))
plt.figure()
plt.axhline(y=0.1, color='gray', linestyle='--')
plt.bar(x, y, color='#E81B23') 

plt.ylim(0, 0.15)

plt.xlabel('Unit Digit', fontsize=24)
plt.ylabel('Proportion', fontsize=24)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

#ax.set_xticks(labels[::4])

figure = plt.gcf()  # get current figure
figure.set_size_inches(18, 9)
# Crop tight (using bbox_inches='tight')
plt.savefig("US_election_2022_Trump.png", bbox_inches='tight')  # Replace "plot.png" with your desired filename

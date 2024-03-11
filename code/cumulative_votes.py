import csv
import numpy as np
from scipy.stats import chisquare

import matplotlib.pyplot as plt


candidate_key = {1:'Taimur Saleem Khan',2:'Jalal Khan',3:'Muhammad Siddique'}
sum_ecl = {}
sum_pti = {}
i=1
with open('PK-79-Unofficial.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count >0:
            R = int(row[0])

            
            for i in range(1,3):
                if candidate_key[i] not in sum_pti:
                    sum_pti[candidate_key[i]] = {}
                sum_pti[candidate_key[i]][R] = float(row[i])
        line_count += 1

i=1
with open('PK-79-official.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count >0:
            R = int(row[0])
            for i in range(1,3):
                if candidate_key[i] not in sum_ecl:
                    sum_ecl[candidate_key[i]] = {}
                sum_ecl[candidate_key[i]][R] = float(row[i])
        line_count += 1

KEYS = list(sum_ecl[candidate_key[i]].keys())
KEYS.sort
labels = KEYS
#print(XX)
cand_taimur = []
cand_jalal = []
for i in KEYS:
    cand_taimur.append(sum_ecl[candidate_key[1]][i])
    cand_jalal.append(sum_ecl[candidate_key[2]][i])
counts = {
    "Taimur Jhagra (ECP)": np.array(cand_taimur),
    "Jalal Khan (ECP)": np.array(cand_jalal),
}

cand_taimur = []
cand_jalal = []
for i in KEYS:
    cand_taimur.append(sum_pti[candidate_key[1]][i])
    cand_jalal.append(sum_pti[candidate_key[2]][i])
counts2 = {
    "Taimur Jhagra (PTI)": np.array(cand_taimur),
    "Jalal Khan (PTI)": np.array(cand_jalal),
}
#colors = ['#cc442c','#dcd878','#9cdc64', '#6c4c7c']
colors = ['#1f77b4','#ff7f0e','#2ca02c','#d62728']
color_index = 0

width = 0.25

width2 = 0.25

bar1 = labels
bar2 = [x + width2 for x in bar1]

fig, ax = plt.subplots()
bottom = np.zeros(len(labels))

for boolean, count in counts.items():
    p = ax.bar(bar1, count, width, label=boolean, bottom=bottom, color=colors[color_index])
    color_index += 1
    bottom += count
bottom = np.zeros(len(labels))

for boolean, count in counts2.items():
    p = ax.bar(bar2, count, width, label=boolean, bottom=bottom, color=colors[color_index])
    color_index += 1
    bottom += count

#ax.set_title("Cumulative Votes", fontsize=36)

plt.xticks(fontsize=16)
plt.yticks(fontsize=24)
plt.legend(fontsize=28,loc="upper right") 
plt.xlabel('Polling Station', fontsize=36)
plt.ylabel('Total Votes', fontsize=36)
#ax.set_xticks(labels[::4])
ax.set_xticks(labels)
figure = plt.gcf()  # get current figure
figure.set_size_inches(32, 12)
# Crop tight (using bbox_inches='tight')
plt.savefig("cumulative_votes_.png", bbox_inches='tight')  # Replace "plot.png" with your desired filename

#plt.show()

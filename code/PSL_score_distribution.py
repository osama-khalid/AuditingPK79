import csv
import numpy as np
from scipy.stats import chisquare
import matplotlib.pyplot as plt


digit_total = {}
i=1
with open('PSL/2022.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
    
        votes = row[0]
        digit = votes[-1]
        if int(votes)>0:
            if digit not in digit_total:
                digit_total[digit] = 0
            digit_total[digit] += 1
        line_count += 1


keys = list(digit_total.keys())
keys.sort()
EXPECTATION = []
OBSERVATION = []
for i in keys:
    OBSERVATION.append(digit_total[i])
    EXPECTATION.append(sum(digit_total.values())/len(digit_total))


print(chisquare(f_obs=OBSERVATION, f_exp=EXPECTATION).pvalue)

x = []
y = []
for i in ['0','1','2','3','4','5','6','7','8','9']:
    x.append(i)
    if i in digit_total:
        y.append(digit_total[i])
    else:
        y.append(0)
plt.axhline(y=sum(digit_total.values())/len(y), color='gray', linestyle='--')
plt.bar(x,y)

plt.ylim(0, 7)

plt.xlabel('Unit Digit', fontsize=24)
plt.ylabel('Frequency', fontsize=24)

plt.xticks(fontsize=16)
plt.yticks(fontsize=24)

#ax.set_xticks(labels[::4])

figure = plt.gcf()  # get current figure
figure.set_size_inches(18, 9)
# Crop tight (using bbox_inches='tight')
plt.savefig("PSL_2022_scores.png", bbox_inches='tight')  # Replace "plot.png" with your desired filename

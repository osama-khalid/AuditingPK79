import csv
import numpy as np
from scipy.stats import chisquare
import matplotlib.pyplot as plt


candidate_key = {1:'Taimur Saleem Khan',2:'Jalal Khan',3:'Muhammad Siddique Afridi'}
digits_ecl = {}
digits_pti = {}
i=1
with open('PK-79-Unofficial.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count >0:
            for i in range(1,4):
                if candidate_key[i] not in digits_pti:
                    digits_pti[candidate_key[i]] = {}
                votes = row[i]
                digit = votes[-1]
                if int(votes)>0:
                    if digit not in digits_pti[candidate_key[i]]:
                        digits_pti[candidate_key[i]][digit] = 0
                    digits_pti[candidate_key[i]][digit] += 1
        line_count += 1

i=1
with open('PK-79-official.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count >0:
            for i in range(1,4):
                if candidate_key[i] not in digits_ecl:
                    digits_ecl[candidate_key[i]] = {}
                votes = row[i]
                digit = votes[-1]
                if int(votes)>0:
                    if digit not in digits_ecl[candidate_key[i]]:
                        digits_ecl[candidate_key[i]][digit] = 0
                    digits_ecl[candidate_key[i]][digit] += 1
        line_count += 1

import numpy as np  
import matplotlib.pyplot as plt  
from scipy.spatial import distance

for key in digits_ecl:
    keys = list(digits_ecl[key].keys())
    keys.sort()
    plt.figure()
    x = []
    y_ecl = []
    y_pti = []
    for i in keys:
        x.append(i)
        y_ecl.append(digits_ecl[key][i]/sum(digits_ecl[key].values()))
        y_pti.append(digits_pti[key][i]/sum(digits_pti[key].values()))

    x = np.arange(len(x)) 
    print(key,1-distance.cosine(y_ecl,y_pti))
    plt.axhline(y=0.1, color='gray', linestyle='--')
    plt.bar(x - 0.2, y_ecl, 0.4, label = 'ECL Forms', color='#E81B23') 
    plt.bar(x + 0.2, y_pti, 0.4, label = 'PTI Forms', color='#00AEF3') 

    if key =='Taimur Saleem Khan':
        plt.ylim(0, max(max(y_ecl),max(y_pti))+0.1)
    else:
        plt.ylim(0, 0.25)
    
    plt.xlabel('Unit Digit', fontsize=24)
    plt.ylabel('Proportion', fontsize=24)
    #plt.title('Unit Digit - My votes in South Punjab', fontsize=24)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    #plt.savefig('2023_Taimur_Official.png')

    plt.xticks(fontsize=16)
    plt.yticks(fontsize=24)

    #ax.set_yticks(labels[::4])

    figure = plt.gcf()  # get current figure
    figure.set_size_inches(18, 9)
    # Crop tight (using bbox_inches='tight')
    plt.savefig(key+"_Combined_forms.png", bbox_inches='tight')  # Replace "plot.png" with your desired filename
    
import csv
import numpy as np
from scipy.stats import chisquare
import matplotlib.pyplot as plt


candidate_key = {1:'Taimur Saleem Khan',2:'Jalal Khan',3:'Muhammad Siddique Afridi'}
digits = {}
i=1
with open('PK-79-official.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count >0:
            for i in range(1,4):
                if candidate_key[i] not in digits:
                    digits[candidate_key[i]] = {}
                votes = row[i]
                digit = votes[-1]
                if int(votes)>0:
                    if digit not in digits[candidate_key[i]]:
                        digits[candidate_key[i]][digit] = 0
                    digits[candidate_key[i]][digit] += 1
        line_count += 1


import numpy as np  
import matplotlib.pyplot as plt  

for key in digits:
    keys = list(digits[key].keys())
    keys.sort()

    EXPECTATION = []
    OBSERVATION = []
    for i in keys:
        OBSERVATION.append(digits[key][i])
        EXPECTATION.append(sum(digits[key].values())/len(digits[key]))
    print(key,chisquare(f_obs=OBSERVATION, f_exp=EXPECTATION).pvalue)

    plt.figure()
    x = []
    y = []
    for i in keys:
        x.append(i)
        y.append(digits[key][i]/sum(digits[key].values()))
    plt.axhline(y=0.1, color='gray', linestyle='--')
    plt.bar(x,y, color='#E81B23')
    if key =='Taimur Saleem Khan':
        plt.ylim(0, max(y)+0.1)
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
    plt.savefig(key+"_ECP_forms.png", bbox_inches='tight')  # Replace "plot.png" with your desired filename
    #plt.show()


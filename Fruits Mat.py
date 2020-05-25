import matplotlib.pyplot as plt

import csv
'''
x=[]
y=[]

with open('fruits.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        x.append(str(row[0]))
        y.append(str(row[1]))

        for line in file:
            split_line=line.split(',')
            if len(split_line)==3:
                if 'Fruits' not in line:
                    file.append(line)


plt.plot(x,y,'o')

plt.show()

'''
with open('fruits.csv', 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        print (line)


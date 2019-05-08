import matplotlib.pyplot as plt
import csv
import numpy as np

dot = []

#read the file
with open('imgur_imagetags.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)  #skip header row
    for row in plots:
        dot.append([int(row[6]), int(row[3]), int(row[7])])  #points, views, comment_count


#assign the graph values
dot.sort()
x = [i[0] for i in dot ]
y = [i[1] for i in dot ]
z = [i[2] for i in dot ]

x1 = [i[0] for i in dot if i[1] > 155000]
y1 = [i[1] for i in dot if i[1] > 155000]

x2 = [i[0] for i in dot if i[1] < 155000]
y2 = [i[1] for i in dot if i[1] < 155000]

#set up the graph
plt.scatter(x, y, s = z*1000, alpha = 0.4, c = z, cmap = 'summer')
plt.xlabel('Points')
plt.ylabel('Views')
plt.title('Comments vs. Views Per Point')
plt.tick_params(labelbottom=True, labelleft=True)

#display values on the graph
#for a,b in zip(x, y): 
#    plt.text(a, b, str(a) + ',' + str(b))


#add trend lines
z1 = np.polyfit(x1, y1, 1)
p1 = np.poly1d(z1)
plt.plot(x1, p1(x1), linewidth = 1, c ='orange')

z2 = np.polyfit(x2, y2, 1)
p2 = np.poly1d(z2)
plt.plot(x2, p2(x2), linewidth = 1, c ='red')

#display the graph	
plt.show()

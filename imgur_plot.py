import matplotlib.pyplot as plt
import csv

dot = []

#read the file
with open('imgur_imagetags.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)  #skip header row
    for row in plots:
        dot.append([int(row[6]), int(row[3]), int(row[7])])  #points, views, comment_count


#assign the graph values
dot.sort()
x = [i[0] for i in dot]
y = [i[1] for i in dot]
z = [i[2] for i in dot]

#print(x)
#print(y)
#print(z)

#set up the graph
plt.scatter(x, y, s = z*1000, alpha = 0.4, c = z, cmap = 'summer')  #seismic  brg  Spectral
plt.xlabel('Points')
plt.ylabel('Views')
plt.title('Comments vs. Views Per Point')
plt.tick_params(labelbottom=True, labelleft=True)

#display values on the graph
#for a,b in zip(x, y): 
#    plt.text(a, b, str(a) + ',' + str(b))

#display the graph
plt.show()

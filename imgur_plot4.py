import matplotlib.pyplot as plt
import csv
import six

dot = []

#read the file
with open('imgur_imagetags.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        dot.append([int(row[6]), int(row[3]), row[2]])  #points, views, image_or_album

#assign the graph values
dot.sort()
x = [i[0] for i in dot]
y = [i[1] for i in dot]
z = [('red' if i[2] == 'Image' else 'blue') for i in dot]  #red is image, blue if album

#set up the graph
plt.scatter(x, y, s = 50, alpha = 0.6, c = z)
plt.xlabel('Points')
plt.ylabel('Views')
plt.title('Images/Albums vs. Views Per Point')
plt.tick_params(labelbottom=True, labelleft=True)

#display the graph
plt.show()

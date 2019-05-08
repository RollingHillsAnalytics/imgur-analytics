import matplotlib.pyplot as plt
import pandas as pd
import six

#read the file
allimages = pd.read_csv('imgur_imagetags.csv', encoding = 'ISO-8859–1')

#filter the input to keep only images with more than 155000 views
images = allimages[allimages['views'] > 155000]

#keep a subset of columns and sort by upload_date
images = images[['image_id', 'upload_date', 'image_or_album', 'views', 'points', 'comment_count', 'tag_count']]
images = images.sort_values(by = ['upload_date'], ascending = [True])

#print(images)

#set up the table as a subplot
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

the_table = ax.table(cellText = images.values, colLabels = images.columns, loc = 'center', cellLoc='center')
the_table.auto_set_font_size(False)
the_table.set_fontsize(10)

#format the header row
for k, cell in six.iteritems(the_table._cells):
    if k[0] == 0:
        cell.set_text_props(weight='bold', color='w')
        cell.set_facecolor('#40466e')

#display the table
plt.show()

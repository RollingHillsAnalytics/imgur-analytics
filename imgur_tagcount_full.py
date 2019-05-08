import pandas as pd

#read in the image and tag files, sort by image_id
images = pd.read_csv('imgur_images.csv', encoding = 'ISO-8859–1')
tags = pd.read_csv('imgur_tags.csv', encoding = 'ISO-8859–1')

sorted_images = images.sort_values(by = ['image_id', 'extract_date'], ascending = [True, False])
sorted_tags = tags.sort_values(by = ['image_id'], ascending = [True])

#eliminate duplicates, keep latest row
deduped_images = sorted_images.drop_duplicates(['image_id'], keep='first')
deduped_tags = sorted_tags.drop_duplicates()

#count the tags and rename the output field
tagcount = deduped_tags.groupby('image_id', as_index = False).count()
tagcount.columns = ['image_id', 'tag_count']

#add the count of tags to the image data
imagetags = pd.merge(deduped_images, tagcount, on = 'image_id', how = 'inner')

#write to file
imagetags.to_csv('imgur_imagetags.csv', index = False, encoding = 'ISO-8859–1')

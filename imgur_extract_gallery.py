import configparser
from imgurpython import ImgurClient
import datetime as dt
import requests
import csv
import sys

extract_date = dt.datetime.now()

#import config file and read in the values
config = configparser.ConfigParser()
config.read('auth.ini')
client_id = config.get('credentials', 'client_id')
client_secret = config.get('credentials', 'client_secret')

#open connection to imgur and retrieve all gallery images
client = ImgurClient(client_id, client_secret)
images = client.gallery()

image_info = []
image_tags = []

print('Processing.', end = '')

#go through the gallery images and record the necessary fields; images and albums are treated differently
for image in images:
	print('.', end = '')
	sys.stdout.flush()
	if image.is_album == True:
		#record fields for this album
		image_info.append([image.id, image.title, 'Album', image.views, image.ups, image.downs, image.points, image.comment_count, str(dt.datetime.fromtimestamp(image.datetime)), str(extract_date)])

		#retrieve tags for the album
		r = requests.get('https://api.imgur.com/3/gallery/album/{}'.format(image.id), headers={'Authorization':'Client-ID {}'.format(client_id)})

		jsonr = r.json()

		#record the tags for this album
		for tag in jsonr['data']['tags']:
			image_tags.append([image.id, tag['display_name']])

	else:
		#record fields for this image
		image_info.append([image.id, image.title, 'Image', image.views, image.ups, image.downs, image.points, image.comment_count, str(dt.datetime.fromtimestamp(image.datetime)), str(extract_date)])

		#retrieve tags for the image
		r = requests.get('https://api.imgur.com/3/gallery/image/{}/tags'.format(image.id), headers={'Authorization':'Client-ID {}'.format(client_id)})

		jsonr = r.json()

		#record the tags for this image
		for tag in jsonr['data']:
			image_tags.append([image.id, tag['display_name']])
		

#write image data to file
with open('imgur_images.csv', 'a', encoding = 'utf-8') as outfile:
	for image in image_info:
		#print(image)
		writer = csv.writer(outfile, lineterminator = '\n')
		writer.writerow(image)
		
#write tags to file
with open('imgur_tags.csv', 'a', encoding = 'utf-8') as outfile:
	for tag in image_tags:
		writer = csv.writer(outfile, lineterminator = '\n')
		writer.writerow(tag)

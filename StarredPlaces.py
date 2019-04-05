#Written by Steven Martinez
#Convert Google Saved Places GeoJSON to CSV
import json
import csv
#GeoJSON in same directory as script
filename = "Saved Places.json"
file = open(filename, "r")
json_parsed = json.load(file)
data = json_parsed.get("features")
#Write a new CSV in the same directory
with open('SavedPlaces.csv','w') as csv_file:
	csvwriter = csv.writer(csv_file)
	count = 0
	for i in data:
		if count == 0:
			#Establish the headers to be written to the CSV
			header = ["Title","Address","Country_Code","Long","Lat","URL"]
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow([i.get('properties').get('Title'),i.get('properties').get('Location').get('Address'),i.get('properties').get('Location').get('Country Code'),i.get('geometry').get('coordinates')[0],i.get('geometry').get('coordinates')[1],i.get('properties').get('Google Maps URL')])
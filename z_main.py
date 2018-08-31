import os
import glob
import shutil
from PyPDF2 import PdfFileMerger
import stat

#Creates Class to work with the airports
class Airport:

	def __init__(self, icao):
		self.chart_types = ''
		self.icao = icao

#PyPDF2 Merger function
def merger(output_path, input_paths):
    pdf_merger = PdfFileMerger()
    file_handles = []
 
    for path in input_paths:
        pdf_merger.append(path)
 
    with open(output_path, 'wb') as fileobj:
        pdf_merger.write(fileobj)

#Gets the list of airports and delete python files from the list
list_of_airports = os.listdir()
list_of_airports.remove("z_main.py")
#list_of_airports.remove("test_del.py")

#initializes an empty list to append the objects from Airport Class
airport = []

#Get airport attributes creating a list of Airport Objects
for i in range(len(list_of_airports)):
	
	airport.append(Airport(list_of_airports[i]))
	airport[i].chart_types = (os.listdir(list_of_airports[i]))

#Paths to work with the merger
paths = ''		

#Here we merge the PDFs obeying the logic - ICAO-CHART.pdf inside each Airport directory
for i in range(len(list_of_airports)):

	for j in range(len(airport[i].chart_types)):
	
		paths = glob.glob(airport[i].icao+'/'+airport[i].chart_types[j]+'/*.pdf')	#Ex: SBAR/IAC/IAC1.pdf, ..IAC2.pdf, and so on
		paths.sort()																#Sort the files

		#Merges the PDFs
		merger(airport[i].icao+'/'+airport[i].icao+'-'+airport[i].chart_types[j]+'.pdf',paths)

for i in range(len(list_of_airports)):

	airport[i].chart_types = [item for item in airport[i].chart_types if not('pdf' in item)]
	for folder in airport[i].chart_types:
		fpath = airport[i].icao+'\\'+folder
		
		os.chmod(fpath, stat.S_IWRITE)
		try:
			shutil.rmtree(fpath)
		except PermissionError:
			try:
				shutil.rmtree(fpath)
			except PermissionError:
				print('Could not delete folder '+fpath)


os.system('pause')
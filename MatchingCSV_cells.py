__Author__ = 'Terrance Randolph'


# import arcpy,csv,os
# from arcpy import env
import csv,os
from pprint import pprint as p 
Dir = "Path/test/"
citydata = "Path/world_cities.csv"
TerrorData = "Path/TerrorData.csv"


def Merge(TerrorData,citydata,Dir):# dict[key:]  =  value
		# Relacing the empty cell with null values.. privious problem solved here..
	with open(TerrorData,'rb') as infile, open(Dir+"CleanTerror.csv", "wb") as outfile:
	    r,w = csv.reader(infile),csv.writer(outfile)
	    w.writerow(next(r))  # Writes the header unchanged
	    for i in r:
	    	i=[x.replace('','N/A') if x == '' else x for x in i]
	    	w.writerow(i)
	    # Creating dict. with City as key..
	TD,CL= {},{}
	with open(Dir+"CleanTerror.csv", 'r') as t, open(citydata, 'r') as c:
	    tfile,cfile = csv.reader(t,delimiter = ","),csv.reader(c,delimiter = ",")
	    terrorHeader,cityHeader = tfile.next(),cfile.next()
	    for i in tfile:
	        TD[i[3]] = i[0:2]+i[4:]
	    for i in cfile:
	        CL[i[1]] = i[2:8]
	    # Establishing the headers new order for the csv document.
	THd = str(terrorHeader[3]).strip('[]'),str(terrorHeader[0:2]).strip('[]'),str(terrorHeader[4:]).strip('[]')
	CHd = str(cityHeader[2:8]).strip('[]')
		# Unique keys are parsed and written to a text file with its corrasponding data...exess files removed.
	with open(Dir+'test.txt', 'w') as f:
		f.write(str(THd).strip('()')+","+str(CHd).strip('()'))
		matchingKeys = set(TD).intersection(CL)
		for i in matchingKeys:
			f.write(str(i)+','+str(TD[i]).strip('[]')+','+str(CL[i]).strip('[]')+"\n")
	with open(new,'r')as f, open(Dir+'tn.txt','w')as j:
		lines = f.read().replace("'",'').replace('"','')  
		j.write(str(lines))	
 	os.rename(Dir+'test.txt',Dir+'Combined.csv')	

Merge(TerrorData,citydata,Dir)

	
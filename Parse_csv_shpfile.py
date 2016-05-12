##import arcpy,csv
##from arcpy import env
##from arcpy.sa import *

Pointfile = "C:\\Users\\terrance\\Desktop\\Homework 4\\tweetsForOctoberFlood.csv"
#Outfile = "E:\\Spatial Programming\\HW4\\"
def parseTweets(Pointfile):
    import csv
    py = None
    try:
        with open(Pointfile,'r') as text:
            next(text)
            lines = csv.reader(text, delimiter = ',')
            tupleList = [i[1:5] for i in lines]
        return tupleList
           
    except IOError as e:
        print(e)
    finally:
        if py != None:
           text.close()     

print('This List has the first: ' + str(len(parseTweets(Pointfile)[:10])) + ' rows.\n')
for i in enumerate(parseTweets(Pointfile)[:10]):
   print(str(i) + '\n')

def countTweets(userID):
    return len([i[0] for i in parseTweets(Pointfile) if i[0]==userID])

print 'The total tweets from: {} is: {}'.format('232398633',countTweets('232398633'))

def generateShapeFile(Pointfile, Outputfile):
   SR = arcpy.SpatialReference(4326)
   tupleList = parseTweets(Pointfile)
   xyList = []
   for i in tupleList:
       if i[1].strip == "" or i[2].strip == "":
           continue
       Points = arcpy.Point(i[1],i[2])
       PointGeometry = arcpy.PointGeometry(Points,SR)
       xyList.append(PointGeometry)
   arcpy.CopyFeatures_management(xyList,Outfile + Outputfile + ".shp")
   return xyList

generateShapeFile(Pointfile, "floods")


arcpy.CheckOutExtension("Spatial")
          
IN = "E:\\Spatial Programming\\HW4\\floods.shp"
Pop = "NONE"
floodDensity = "E:\\Spatial Programming\\HW4\\floodDensity"
outputDensity = arcpy.sa.PointDensity(IN, Pop)
outputDensity.save(floodDensity)






















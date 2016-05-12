

#file1 = "C:\\Users\\GovInfoMaps2\\Desktop\\GPS_Trackpoints.txt"
print('         Terrance Randolph Homework 3\n\n')
print('Example...C:\Users\GovInfoMaps2\Desktop\GPS_Trackpoints.txt\n')
text = raw_input('Enter GPS_Trackpoint file: ' )
file1 = text.replace("\\","\\\\")

#####################
### Question 3
def parseGPS_Trackpoint1(file1):
    import string
    print('Question 3\n')
    try:
        with open(file1,'r') as text:
                readTxt = text.readlines()
                for line in readTxt[1:len(readTxt)]:
                    point = line.split(',')
                    pointID = point[0]
                    Longitude = point[1]
                    Latitude = point[2]
                    Altitude = point[3]
                    Time = point[4]
                    print('Point'+str(pointID)+' Longitude '+str(Longitude)+
                          ' Latitude '+str(Latitude)+
                  	  ' Altitude '+str(Altitude)+'m')
    except IOError as e:
        print(e)
parseGPS_Trackpoint1(file1)

#####################
######Question 5#####
def parseGPS_Trackpoint(file1):
    import string
    from HW3_RandolphTerrance import GPSPoint
    try:
        gpsPointList=[]
        with open(file1,'r') as text:
                readTxt = text.readlines()
                for line in readTxt[1:len(readTxt)]:
                    point = line.split(',')
                    GPS_Pt = GPSPoint(int(point[0]), 
                                       float(point[1]),
                                       float(point[2]),
                                       float(point[3]),
                                       point[4])
                    gpsPointList.append(GPS_Pt)
        return gpsPointList
        
    except IndentationError as e:
        print(e)
#parseGPS_Trackpoint(file1)

#########################
####### Question 6 ######
##

from HW3_RandolphTerrance import GPSPoint
print('\nQuestion 6')
gpsPointList = parseGPS_Trackpoint(file1)
sumAltitude = 0
print '____________ALTITUDE IN FEET____________'
for gpsPoint in gpsPointList:
    AltPoint= gpsPoint.Altitude
    PointCount = gpsPoint.pointID
    AltFeet = gpsPoint.getAltitudeInFeet(AltPoint)
    sumAltitude =  sumAltitude + AltFeet
    print('Point: ' + str(PointCount) +
           '   Altitude: ' + str(AltPoint) +
           '  converted to feet is: '+ str(AltFeet))
    sumAltitude += 1
Advg = sumAltitude / len(gpsPointList)
print('\n' + 
         '     The combined altitude is: ' + str(sumAltitude) + ' = int: ' + str(int(sumAltitude)) + 
         '\n' + 
         '     The adverage altitude is: ' + str(Advg) + ' = int: ' + str(int(Advg)) )


# ########################
# ##   Question 7 #######
# #get distance 005 to 008

from HW3_RandolphTerrance import GPSPoint
print('\nQuestion 7')
print'____________DISTANCE__________'
a = []
gpsPointList = parseGPS_Trackpoint(file1)
for gpsPoint in gpsPointList[4:len(gpsPointList)]:
    LongLat = gpsPoint.Longitude,gpsPoint.Latitude
    a.append(LongLat)
for pt in a:
    distance = gpsPoint.getDistance(a[0][0],a[0][1],a[3][0],a[3][1])
print ' Point 005:' + str(a[0][0]),str(a[0][1])
print ' Point 008: ' + str(a[3][0]),str(a[3][1])
print '     Total distance : ' + str(distance)+ '\n      As an int : ' + str(int(distance))



########################
###display attributes##
from HW3_RandolphTerrance import GPSPoint
print('\nExtra, using display fuction!\n')
gpsPointList = parseGPS_Trackpoint(file1)
for gpsPoint in gpsPointList:
    GPSPoint(gpsPoint.pointID, gpsPoint.Longitude,
             gpsPoint.Latitude, gpsPoint.Altitude,
             gpsPoint.Time).display()



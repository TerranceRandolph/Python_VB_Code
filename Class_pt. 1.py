#	Terrance Randolph
#		Homework 3


###################
###	question 4 ###
class GPSPoint(object):
	def __init__ (self, pointID,Longitude,Latitude,Altitude,Time):
		self.pointID = pointID
		self.Longitude = Longitude
		self.Latitude = Latitude
		self.Altitude = Altitude
		self.Time = Time
	

	def display(self):
		try:
			print(self.pointID,(self.Longitude,self.Latitude),self.Altitude,self.Time)
		except Exception as e:
			print(e)
			print('Paramerters maybe wrong.')

	def getDistance(self,Longitude1,Latitude1,Longitude2,Latitude2):
		from math import cos, asin, sqrt 
		try:
			p = 0.017453292519943295
			a = 0.5 - cos((Latitude2 - Latitude1) * p)/2 + cos(Latitude1 * p) * cos(Latitude2 * p) *(1 - cos((Longitude2 - Longitude1) * p)) / 2
			c = 12742 * asin(sqrt(a))
			return c 
		except Exception as e:
			print(e)

	def getAltitudeInFeet(self,Altitude):
		# 1meter=3.28 == 1*3.280839895 
		try:
			feet = 3.28
			conversion = float(Altitude) * float(feet)
			return conversion
		except Exception as e:
			print(e)

if '__name__' == '__main__':
        main() 

print('         Terrance Randolph Homework 3\n\n')
print("Open 'HW_3 TerranceRandolph'to see GPSPoint class")

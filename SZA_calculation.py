from pysolar import solar
import pandas as pd

lon = -2.3636 #pick a longitude
lat = 37.0916 #pick a latitude
datetime = pd.to_datetime('2004-01-09 16:22:00+00:00') #pick a datetime
date = datetime.to_pydatetime() #transformed to the right form
SZA = round(90 - solar.get_altitude(lat,lon,date), 5) #calculate the Solar Zenith Angle

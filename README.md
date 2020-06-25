# Calculating distance, bearing and midpoint between two locations on earth using the haversine formula

1 - This program will calculate the distance between two locations on Earth given their coordinates. 

2 - In order to do this, the program will assume that the Earth is spherical and not elliptical. 

3 - The "haversine" formula will be used to calculate the distance over the surface of the earth between the given two pairs of coordinates. 

4 - The two pairs of coordinates should be entered by the user in Latitude and Longitude formats. 

5 - Latitude and Longitude formats should be:

    Decimal degrees without compass direction. 
    
    With negative indicating west/south: e.g. 33.7655, -72.8365
    
6 - The program will check if the input coordinates are valid and if they are the correct type

7 - The  haversine formula calculates the distance between the two points on the earth 

    by multiplying the mean radius of the earth by the angular distance of the points in radians. 
    
8 - Being: Distance = R x C

9 - Mean radius of the earth (R) = 6,371.0088 km

10- Angular distance in radians (C) = 2 ⋅ atan2( √a, √(1−a) )

11- Being a (the square of half the chord length between the points) = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)

12- Where: φ is latitude, λ is longitude, Δφ is Lat2-Lat1 and Δλ is Long2-Long1


This way:

a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)

c = 2 ⋅ atan2( √a, √(1−a) )

D = R ⋅ c




13- The output of the program is:

    a) the distance between the two points in meters (no decimals), kilometers (2 decimals) and miles (2 decimals). 
    
    b) the initial and final bearings (on the extra credit section)
    
    c) the midpoint coordinates between the two locations (extra credit section)
    

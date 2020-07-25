# The Smart Earthquake System (SES) project: 
## developing a location-based risk factor
<br>

- ### Project goal:

To predict the safe/vulnerable situation of a location and home to Earthquakes.

- ### Project goal:

A decision maker who decides to value a place based on Earthquake probability maps

- ### System design:


- a: Gets the earthquake data from USGS (Earthquake depth, focal mechanism, magnitude, location, time). Gets the real-time continuous signals from IRIS.<br>
- b: Does analyze the locations real-time, clustering spatial of the data, and try matching them with the fault structures that are derived in maps.<br>
- c: Shows the location of current Earthquakes, faults, and risk factors.<br>
- d: Shows the risk factors in nearby business venues and homes.<br>
- e: Build a location-based (get Street address find in google map) risk factor based on observations.<br>


- ### [USGS API](https://earthquake.usgs.gov/fdsnws/event/1/#methods):
So, keeping all the things in mind, I have decided to go with the United States Geological Survey(USGS) for earthquake data. USGS provides a very intuitive, easy-to-use, reliable API and web portal service, which provides flexibility in output format, specifying regions of interest and more. USGS is a government operated research center and the data they provide are free of cost and are very reliable because most of them are reviewed by human before their registration. The API request link does not require any authentication.
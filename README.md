# Time-series based analysis of Earthquake Risk Factors
## A practical approach for risk analysis of the "Big One"
<br>

- ### Project goal:

Or goal is to predict the safe/vulnerable situation of a location and home to Earthquakes. Several potential clients such as a decision maker who decides to value a house based on Earthquake probability maps could immediately benefit from this model.

- ### System design:


- a: Gets the earthquake data from USGS (Earthquake depth, focal mechanism, magnitude, location, time). Gets the real-time continuous signals from IRIS.<br>
- b: Does analyze the locations real-time, clustering spatial of the data, and try matching them with the fault structures that are derived in maps.<br>
- c: Shows the location of current Earthquakes, faults, and risk factors.<br>
- d: Shows the risk factors in nearby business venues and homes.<br>
- e: Build a location-based (get Street address find in google map) risk factor based on observations.<br>


- ### [USGS API](https://earthquake.usgs.gov/fdsnws/event/1/#methods): Also, important [link](https://earthquake.usgs.gov/data/comcat/data-eventterms.php#rms)
So, keeping all the things in mind, I have decided to go with the United States Geological Survey(USGS) for earthquake data. USGS provides a very intuitive, easy-to-use, reliable API and web portal service, which provides flexibility in output format, specifying regions of interest and more. USGS is a government operated research center and the data they provide are free of cost and are very reliable because most of them are reviewed by human before their registration. The API request link does not require any authentication.

- Some links:
https://www.miamiherald.com/news/nation-world/national/article244851172.html

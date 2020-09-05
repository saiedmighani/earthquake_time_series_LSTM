### Data parameters from USGS API documentary:

https://earthquake.usgs.gov/data/comcat/data-eventterms.php#depthError


json dictionary keys:

   dict_keys(['type', 'metadata', 'features', 'bbox'])



1 - "type": FeatureCollection

2 - "metadata": 

  "generated": 1599234383000,<br>
  "url": "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=1989-10-15&endtime=1989-10-19&minmagnitude=1&maxmagnitude=10&minlatitude=32&maxlatitude=42&minlongitude=-126&maxlongitude=-114&orderby=time&limit=2000",<br>
  "title": "USGS Earthquakes",<br>
  "status": 200,<br>
  "api": "1.10.3",<br>
  "limit": 2000,<br>
  "offset": 1,<br>
  "count": 1038<br>

3 - "features":<br>
    Feature:<br><br>
        "mag": 1.42,<br>
        Description: The magnitude for the event. See also magType.<br><br>
        "place": "Northern California",<br>
        Description: Textual description of named geographic region near to the event. This may be a city name, or a Flinn-Engdahl Region name.<br><br>
        "time": 624757977010,<br>
        Description: Time when the event occurred. Times are reported in milliseconds since the epoch ( 1970-01-01T00:00:00.000Z), and do not include leap seconds. In certain output formats, the date is formatted for readability.<br><br>
        "updated": 1481291793752,<br>
        Description: Time when the event was most recently updated. Times are reported in milliseconds since the epoch. In certain output formats, the date is formatted for readability.
        "tz": null,<br>
        Description: Timezone offset from UTC in minutes at the event epicenter.<br><br>
        "url": "https://earthquake.usgs.gov/earthquakes/eventpage/nc263323",<br>
        Description: Link to USGS Event Page for event.<br><br>
        "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=nc263323&format=geojson",<br>
        Description: Link to GeoJSON detail feed from a GeoJSON summary feed.<br><br>
        "felt": null,<br>
        Description: The total number of felt reports submitted to the DYFI? system.<br><br>
        "cdi": null,<br>
        Description: The maximum reported intensity for the event. Computed by DYFI. While typically reported as a roman numeral, for the purposes of this API, intensity is expected as the decimal equivalent of the roman numeral. Learn more about magnitude vs. intensity.<br><br>
        "mmi": null,<br>
        Description: The maximum estimated instrumental intensity for the event. Computed by ShakeMap. While typically reported as a roman numeral, for the purposes of this API, intensity is expected as the decimal equivalent of the roman numeral.<br><br>
        "alert": null,<br>
        Description: The alert level from the PAGER earthquake impact scale.<br><br>
        "status": "reviewed",<br>
        Description: Indicates whether the event has been reviewed by a human.<br><br>
        "tsunami": 0,<br>
        Description: This flag is set to "1" for large events in oceanic regions and "0" otherwise. The existence or value of this flag does not indicate if a tsunami actually did or will exist.<br><br>
        "sig": 31,<br>
        Description: A number describing how significant the event is. Larger numbers indicate a more significant event. This value is determined on a number of factors, including: magnitude, maximum MMI, felt reports, and estimated impact.<br><br>
        "net": "nc",<br>
        Description: The ID of a data contributor. Identifies the network considered to be the preferred source of information for this event.<br><br>
        "code": "263323",<br>
        Description: An identifying code assigned by - and unique from - the corresponding source for the event.<br><br>
        "ids": ",nc263323,",<br>
        Description: A comma-separated list of event ids that are associated to an event.<br><br>
        "sources": ",nc,",<br>
        Description: A comma-separated list of network contributors.<br><br>
        "types": ",nearby-cities,origin,phase-data,",<br>
        Description: A comma-separated list of product types associated to this event.<br><br>
        "nst": 11,<br>
        Description: The total number of seismic stations used to determine earthquake location.<br><br>
        "dmin": 0.02342,<br>
        Horizontal distance from the epicenter to the nearest station (in degrees). 1 degree is approximately 111.2 kilometers. In general, the smaller this number, the more reliable is the calculated depth of the earthquake.<br><br>
        "rms": 0.03,<br>
        Description: The root-mean-square (RMS) travel time residual, in sec, using all weights. This parameter provides a measure of the fit of the observed arrival times to the predicted arrival times for this location. Smaller numbers reflect a better fit of the data.<br><br>
        "gap": 70,<br>
        Description: The largest azimuthal gap between azimuthally adjacent stations (in degrees). In general, the smaller this number, the more reliable is the calculated horizontal position of the earthquake.<br><br>
        "magType": "md",<br>
        Description: The method or algorithm used to calculate the preferred magnitude for the event.<br><br>
"type": "earthquake",<br>
Description: Type of seismic event.<br><br>
        "title": "M 1.4 - Northern California"<br><br>
        Geometry:<br>
        "type": "Point",<br>
        "coordinates": [-121.9451667, 37.1483333, 6.129]<br>
        id:<br><br>
   4 - "bbox":<br>
    [-123.623, 32.459, -1.75, -114.78, 40.8645, 27.625]<br>

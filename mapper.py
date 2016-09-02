#Python 2.x:
#
import urllib
import urllib2
import json
import pprint
#urllib2.urlopen("http://example.com/foo/bar").read()
#Python 3.x:
#
#import urllib.request
#urllib.request.urlopen("http://example.com/foo/bar").read()


header = """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Heatmaps</title>
    <style>
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
      #map {
        height: 100%;
      }
      #panel {
        background-color: #fff;
        border: 1px solid #999;
        left: 25%;
        padding: 5px;
        position: absolute;
        top: 10px;
        z-index: 5;
      }
    </style>
  </head>

  <body>
    <div id="panel">
      <button onclick="toggleHeatmap()">Toggle Heatmap</button>
      <button onclick="changeGradient()">Change gradient</button>
      <button onclick="changeRadius()">Change radius</button>
      <button onclick="changeOpacity()">Change opacity</button>
    </div>
    <div id="map"></div>
    <script>

var map, heatmap;

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 13,
    center: {lat: 37.775, lng: -122.434},
    mapTypeId: google.maps.MapTypeId.SATELLITE
  });

  heatmap = new google.maps.visualization.HeatmapLayer({
    data: getPoints(),
    map: map
  });
}

function toggleHeatmap() {
  heatmap.setMap(heatmap.getMap() ? null : map);
}

function changeGradient() {
  var gradient = [
    'rgba(0, 255, 255, 0)',
    'rgba(0, 255, 255, 1)',
    'rgba(0, 191, 255, 1)',
    'rgba(0, 127, 255, 1)',
    'rgba(0, 63, 255, 1)',
    'rgba(0, 0, 255, 1)',
    'rgba(0, 0, 223, 1)',
    'rgba(0, 0, 191, 1)',
    'rgba(0, 0, 159, 1)',
    'rgba(0, 0, 127, 1)',
    'rgba(63, 0, 91, 1)',
    'rgba(127, 0, 63, 1)',
    'rgba(191, 0, 31, 1)',
    'rgba(255, 0, 0, 1)'
  ]
  heatmap.set('gradient', heatmap.get('gradient') ? null : gradient);
}

function changeRadius() {
  heatmap.set('radius', heatmap.get('radius') ? null : 20);
}

function changeOpacity() {
  heatmap.set('opacity', heatmap.get('opacity') ? null : 0.2);
}

// Heatmap data: 500 Points
function getPoints() {
  return [ """
  
  
tail = """ ];
}

    </script>
    <script async defer
        src="https://maps.googleapis.com/maps/api/js?
signed_in=true&libraries=visualization&callback=initMap">
    </script>
  </body>
</html>"""

middle = ""
count = 0
with open("OCR Race Schedule - Sheet1.csv", "r") as f:
    next(f)
    for line in f:
        inner = line.split(",")
        if int(inner[0]) == 1:
            address = "http://geocoder.maplarge.com/geocoder/json?address="+str(inner[4])+"&city="+str(inner[5])+"&state="+str(inner[6])+"&zip="+str(inner[7])+"&country=US&key=YOUR_API_KEY"
            #address = urllib.urlencode("test")            
            address = address.replace(" ", "%20")
            
            j = json.loads(urllib2.urlopen(address).read())
            #pprint.pprint(j)
            #input("test 1")            
            gLine = "new google.maps.LatLng("+str(j["lat"])+","+str(j["lng"])+")"
            middle = middle + gLine + ", "
            count = count + 1
middle = middle[:-1]
print("Count: ", str(count))
#input("test")
output = open("ocr_heatmap.html", "w")
output.write(header+middle+tail)

output.close()


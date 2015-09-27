
var gMap;
var strMapDivName = "gmap";
var haightAshbury = {lat: 37.769, lng: -122.446};
var markers = [];



function initMap() {
    detectBrowser();

    gMap = new google.maps.Map(document.getElementById(strMapDivName), {
        center: {lat: 21, lng: 78},
        mapTypeId: google.maps.MapTypeId.HYBRID,
        zoom: 6,
        heading: 90,
        tilt: 0
    });
    
    // This event listener will call addMarker() when the map is clicked.
    gMap.addListener('click', function(event) {
        addMarker(event.latLng);
    });
    
    // Add dragging event listeners.
    gMap.addListener('dragstart', function(event) {
        //updateMarkerAddress('Dragging...');
    });
    
    // Load label.js afterwards so we can be sure that the google maps api has loaded
    var fileref=document.createElement('script')
    fileref.setAttribute("type","text/javascript")
    fileref.setAttribute("src", "js/label.js")
    
    document.getElementsByTagName("head")[0].appendChild(fileref)
    
}

function detectBrowser() {
    var useragent = navigator.userAgent;
    var mapdiv = document.getElementById(strMapDivName);

    if (useragent.indexOf('iPhone') != -1 ||
        useragent.indexOf('Android') != -1 ) {
        mapdiv.style.width = '100%';
        mapdiv.style.height = '100%';
    } else {
       // mapdiv.style.width = '100%';
       // mapdiv.style.height = '100%';
    }
}

var latlngToPoint = function(map, latlng, z){
	var normalizedPoint = map.getProjection().fromLatLngToPoint(latlng); // returns x,y normalized to 0~255
	var scale = Math.pow(2, z);
	var pixelCoordinate = new google.maps.Point(normalizedPoint.x * scale, normalizedPoint.y * scale);
	return pixelCoordinate; 
};

// Adds a marker to the map and push to the array.
function addMarker(location) {
    var marker = new google.maps.Marker({
        position: location,
        map: gMap,
        draggable: true
    });
    markers.push(marker);
    
    // On click event
    marker.addListener('click', function() {
        //gMap.setZoom(8);
        var pos = marker.getPosition();
        //gMap.setCenter(marker.getPosition());
        
        //var p = latlngToPoint(gMap, pos, gMap.getZoom());
        
        var scale = Math.pow(2, gMap.getZoom());
var nw = new google.maps.LatLng(
    gMap.getBounds().getNorthEast().lat(),
    gMap.getBounds().getSouthWest().lng()
);
var worldCoordinateNW = gMap.getProjection().fromLatLngToPoint(nw);
var worldCoordinate = gMap.getProjection().fromLatLngToPoint(marker.getPosition());
var p = new google.maps.Point(
    Math.floor((worldCoordinate.x - worldCoordinateNW.x) * scale),
    Math.floor((worldCoordinate.y - worldCoordinateNW.y) * scale)
);

        var div = document.getElementById("nodeinfo")
        div.style.position = "relative";
        div.style.left = p.x + 'px';
        div.style.top = p.y + 'px';
    });
    

    // Add dragging event listeners.
    google.maps.event.addListener(marker, 'dragstart', function() {
        //console.debug('Drag start...');

    });
    
    google.maps.event.addListener(marker, 'drag', function() {
        //console.debug('Dragging...');
        //marker.setLabel("Dragging");
        
        //updateMarkerStatus('Dragging...');
        //updateMarkerPosition(marker.getPosition());
    });
  
    google.maps.event.addListener(marker, 'dragend', function() {
        //console.debug('Drag end...');
        //updateMarkerStatus('Drag ended');
        //geocodePosition(marker.getPosition());
        /*var div = document.getElementById("mylabel")
        div.style.display = 'none';*/
    });
    

    // Label for each marker
    var label = new Label({
        map: gMap
    });
    label.bindTo('position', marker, 'position');
    label.bindTo('text', marker, 'position');
}

function geocodePosition(pos) {
  geocoder.geocode({
    latLng: pos
  }, function(responses) {
    if (responses && responses.length > 0) {
      updateMarkerAddress(responses[0].formatted_address);
    } else {
      updateMarkerAddress('Cannot determine address at this location.');
    }
  });
}





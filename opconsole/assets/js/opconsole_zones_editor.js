     // Note: This example requires that you consent to location sharing when
      // prompted by your browser. If you see the error "The Geolocation service
      // failed.", it means you probably did not give permission for the browser to
      // locate you.


var defPos = {lat: 0, lng: 0};
var currPos = defPos;
var gmap_handle = undefined;
var CKS_INDEX_MAP_LAT = "googlemapreivouspos_latidue";
var CKS_INDEX_MAP_LOG = "googlemapreivouspos_longitude";
var ZONES = undefined;
var searchBox = undefined;
var markers = [];

function clearZone() {
        if ( ZONES !== undefined ) {
            ZONES.setMap(null);
            ZONES = undefined;
        }
        $("#btnClearZone").hide();
        $("#btnSaveZone").hide();
        $("#colorPicker").hide();
        $("#btnNewZone").show();
      }
function csrfSafeMethod(method) {
// these HTTP methods do not require CSRF protection
return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function setGeoloc(gmap) {
if ( navigator.geolocation) {
    navigator.geolocation.watchPosition(function(position) {

        Cookies.set(CKS_INDEX_MAP_LAT,  position.coords.latitude  );
        Cookies.set(CKS_INDEX_MAP_LOG,  position.coords.longitude  );

        gmap.setCenter(getCoords(position.coords.latitude,position.coords.longitude))
    });
} else {
    console.log("Unable to retrieve geolocalization, browser doesn't support it")
    gmap.setCenter(getCoords(defPos.lat, defPos.long));
}
}
function getCoords(lat , long) { return new google.maps.LatLng(lat, long); }
function saveZone() {
if ( ZONES !== undefined ) {
    var bounds = ZONES.getBounds();
    dialog.dialog("open");
   }
}
function setCookieGeoloc() {
if ( Cookies.get(CKS_INDEX_MAP_LAT) == undefined ||
     Cookies.get(CKS_INDEX_MAP_LOG) == undefined ) {
        setGeoloc(gmap_handle);
 } else {
    latitude = Cookies.get(CKS_INDEX_MAP_LAT);
    longitude = Cookies.get(CKS_INDEX_MAP_LOG);
    gmap_handle.setCenter(getCoords(latitude,longitude));
 }

}
function newZone() {


xmargin = 0.005;
ymargin = 0.005;

ne_lat = gmap_handle.getBounds().getNorthEast().lat() - xmargin;
ne_lng = gmap_handle.getBounds().getNorthEast().lng() - ymargin;
sw_lat = gmap_handle.getBounds().getSouthWest().lat() + xmargin;
sw_lng = gmap_handle.getBounds().getSouthWest().lng() + ymargin;

ne = getCoords(ne_lat,ne_lng);
sw = getCoords(sw_lat,sw_lng);



var bounds = new google.maps.LatLngBounds(sw,ne);


ZONES = new google.maps.Rectangle({
  editable: true,
  draggable:true,
  strokeColor: '#FF0000',
  strokeOpacity: 0.8,
  strokeWeight: 2,
  map:gmap_handle,
  fillColor: '#FF0000',
  bounds:bounds
});




$("#btnSaveZone").show();
$("#btnClearZone").show();
$("#colorPicker").show();
$("#btnNewZone").hide();
}
function searchBoxLstnr() {
    var places = searchBox.getPlaces();

    if (places.length == 0) { return; }


      markers.forEach(function(marker) {
        marker.setMap(null);
      });
      markers = [];


      var bounds = new google.maps.LatLngBounds();
      places.forEach(function(place) {
        if (!place.geometry) {
          console.log("Returned place contains no geometry");
          return;
        }
        var icon = {
          url: place.icon,
          size: new google.maps.Size(71, 71),
          origin: new google.maps.Point(0, 0),
          anchor: new google.maps.Point(17, 34),
          scaledSize: new google.maps.Size(25, 25)
        };

        // Create a marker for each place.
        markers.push(new google.maps.Marker({
          map: gmap_handle,
          icon: icon,
          title: place.name,
          position: place.geometry.location
        }));

        if (place.geometry.viewport) {
          // Only geocodes have viewport.
          bounds.union(place.geometry.viewport);
        } else {
          bounds.extend(place.geometry.location);
        }
      });
      gmap_handle.fitBounds(bounds);
 }
function initMap() {
    gmap_handle = new google.maps.Map(document.getElementById('map'), {
      center: {lat: -33.8688, lng: 151.2195},
      zoom: 13,
      mapTypeId: 'roadmap'
    });

    searchBox = new google.maps.places.SearchBox(document.getElementById('pac-input'))
    gmap_handle.addListener('bounds_changed', function() { searchBox.setBounds(gmap_handle.getBounds()); });
    searchBox.addListener('places_changed',searchBoxLstnr);
    setCookieGeoloc();
}
var dialog = $( "#save-message" ).dialog({
    autoOpen: false,
    buttons: {
        "Cancel" : function () {
            dialog.dialog("close");
        },
        "Save" : function() {
            zoneName = $("#zone_name").val();
            if (  zoneName !== "" && ZONES !== undefined ) {
                $.post("/zones/new/", {
                    name:zoneName,
                    x1 : ZONES.getBounds().getNorthEast().lat,
                    y1 : ZONES.getBounds().getNorthEast().lng,
                    x2 : ZONES.getBounds().getSouthWest().lat,
                    y2 : ZONES.getBounds().getSouthWest().lng
                })
                .done(function(success) {
                    window.location.replace("/zones/");
                }).fail(function(error) {
                    console.log("unable to send POST request!");

                });
                dialog.dialog("close");
            }

        }
    }
});
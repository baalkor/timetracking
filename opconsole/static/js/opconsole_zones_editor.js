     // Note: This example requires that you consent to location sharing when
      // prompted by your browser. If you see the error "The Geolocation service
      // failed.", it means you probably did not give permission for the browser to
      // locate you.


      var defPos = {lat: 0, lng: 0};
      var currPos = defPos;
      var GMAP_ELEM = document.getElementById('map');
      var gmap_handle;
      var CKS_INDEX_MAP_LAT = "googlemapreivouspos_latidue";
      var CKS_INDEX_MAP_LOG = "googlemapreivouspos_longitude";
      var ZONES = undefined;


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



     function getCoords(lat,long) {
        return new google.maps.LatLng(lat, long)
     }
     function initMap() {


       map = new google.maps.Map(GMAP_ELEM, {
            zoom:13,
            center:defPos
        });
        gmap_handle = map;

        if ( Cookies.get(CKS_INDEX_MAP_LAT) == undefined ||
             Cookies.get(CKS_INDEX_MAP_LOG) == undefined ) {


            setGeoloc(map);
         } else {
            latitude = Cookies.get(CKS_INDEX_MAP_LAT);
            longitude = Cookies.get(CKS_INDEX_MAP_LOG);
            map.setCenter(getCoords(latitude,longitude));
         }




      }

      function saveZone() {
        if ( ZONES !== undefined ) {
            var bounds = ZONES.getBounds();
            dialog.dialog("open");
           }
      }

      function newZone() {

      /*
        margin = 0;
        ne_lat = gmap_handle.getBounds().getNorthEast().lat + margin;
        ne_lng = gmap_handle.getBounds().getNorthEast().lng + margin;
        sw_lat = gmap_handle.getBounds().getSouthWest().lat - margin;
        sw_lng = gmap_handle.getBounds().getSouthWest().lng - margin;

        ne = getCoords(ne_lat,ne_lng);
        sw = getCoords(sw_lat,sw_lng);

        var bounds = new google.maps.LatLngBounds(ne,sw);
        */

        ZONES = new google.maps.Rectangle({
          editable: true,
          draggable:true,
          strokeColor: '#FF0000',
          strokeOpacity: 0.8,
          strokeWeight: 2,
          map:gmap_handle,
          fillColor: '#FF0000',
          bounds:gmap_handle.getBounds()
        });




        $("#btnSaveZone").show();
        $("#btnClearZone").show();
        $("#btnNewZone").hide();
      }

      function clearZone() {
        if ( ZONES !== undefined ) {
            ZONES.setMap(null);
            ZONES = undefined;
        }
        $("#btnClearZone").hide();
        $("#btnSaveZone").hide();
        $("#btnNewZone").show();
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
                $.post("/zones/new", {
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
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$(document).ready(function() {
    $("#btnClearZone").hide();
    $("#btnSaveZone").hide();

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", Cookies.get("csrftoken"));
            }
        }
    });

});

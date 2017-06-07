     // Note: This example requires that you consent to location sharing when
      // prompted by your browser. If you see the error "The Geolocation service
      // failed.", it means you probably did not give permission for the browser to
      // locate you.


      var defPos = {lat: 0, lng: 0};
      var currPos = defPos;
      var GMAP_ELEM = document.getElementById('map');
      var gmap_handle;
      var ZONES = undefined;
      var GOOGLE_API_KEY = "AIzaSyAlXMWGO1qTvsWIxo0W5bUloL0HzknfuOY"
      var mapId = window.location.pathname;

     function getCoords(lat,long) {
        return new google.maps.LatLng(lat, long)
     }

     function removeZone() {
        $.ajax({
            url : "/api"  + mapId,
            type:'DELETE',
            success:function(data)  {
                console.log("Zone removed");
                window.location.replace("/zones/");
            }
        });
     }

     function initMap() {

       $.get("/api"  + mapId ).success(function(data)  {
            console.log(data.color);
            gmap_handle = new google.maps.Map(GMAP_ELEM, {zoom:13,center:defPos,strokeColor:data.color});
            gmap_handle.setCenter(getCoords(data.x1, data.y1));
            drawZoneAt(data.x1,data.y1,data.x2,data.y2);

       });
     }



      function drawZoneAt(ne_lat, ne_lng, sw_lat, sw_lng) {

        bounds = new google.maps.LatLngBounds(getCoords(sw_lat,sw_lng),getCoords(ne_lat,ne_lng))
        ZONES = new google.maps.Rectangle({
          editable: false,
          draggable:false,
          strokeColor: '#FF0000',
          strokeOpacity: 0.8,
          strokeWeight: 2,
          map:gmap_handle,
          fillColor: '#FF0000',
          bounds:bounds
        });


      }




function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$(document).ready(function() {
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", Cookies.get("csrftoken"));
            }
        }
    });

});

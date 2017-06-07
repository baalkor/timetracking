var gmap_handle = undefined;
function initMap() {
    gmap_handle = new google.maps.Map(
    document.getElementById('map'), {
      center: {lat: -33.8688, lng: 151.2195},
      zoom: 13,
      mapTypeId: 'roadmap'
    });
}

$(document).ready(function(){
    setUpCSRFHeader();
    var url = window.location.pathname;
    var tmsId = url.split("/")[2];


    $.ajax({
        method:"POST",
        type:"POST",
        url:"/api/timestamp/",
        data:{"id":tmsId},
        success:function(data) {
            gmap_handle.setCenter(new google.maps.LatLng(
                data.latitude,data.longitude
             ));
          var marker = new google.maps.Marker({
          position: new google.maps.LatLng(
                data.latitude,data.longitude
             ),
          map: gmap_handle,
          title: 'Hello World!'
        });

        }
    })

});
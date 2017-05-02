function removeDevice(devId) {

    $.ajax({
        type:"POST",
        url:"/api/device/remove/",
        data:{id:devId},
        success:function() {location.reload();},

    });
}

function getDevType() {
    var url = window.location.pathname;

    var devId = url.split("/")[2];
    $.get("/api/device/" + devId).done(function(data){console.log(data);});
}

$(document).ready(setUpCSRFHeader());

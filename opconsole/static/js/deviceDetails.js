function removeDevice(devId) {

    $.ajax({
        type:"POST",
        url:"/api/device/remove/",
        data:{id:devId},
        success:function() {console.log("Device removed");},

    });


}

$(document).ready(setUpCSRFHeader());

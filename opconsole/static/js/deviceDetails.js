function removeDevice(devId) {

    $.ajax({
        type:"POST",
        url:"/api/device/remove/",
        data:{id:devId},
        success:function() {location.reload();},

    });
}

function requestSuperCookie() {
    Cookies.set("DEV_KEY",devKey);
    $("#requestSuperCookie").prop('disabled', true);
    $("#requestSuperCookie").text("Done.")
}
var devKey = "";
$(document).ready(function() {

    setUpCSRFHeader();
    var url = window.location.pathname;

    var devId = url.split("/")[2];
    $.get("/api/device" ,  { id:devId }   ).done(function(data){
        if ( data.devType == "1" ) {
            devKey = data.devKey;
            $("#requestSuperCookie").show()
            if (Cookies.get("DEV_KEY") != data.devKey ) {
                $("#error").text( "Warning, current browser key is not matching our records.You will not be able to timestamp with this browser." )
            }

        } else {
            $("#requestSuperCookie").hide()

        }




    });


});

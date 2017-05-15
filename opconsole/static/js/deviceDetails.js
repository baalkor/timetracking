function removeDevice(devId) {

    $.ajax({
        type:"POST",
        url:"/api/device/remove/",
        data:{id:devId},
        success:function() {location.reload();},

    });
}

function deviceToggle(devId) {
    $.ajax({
        type:"POST",
        url:"/api/device/toggle/",
        data:{id:devId},
        success:function() {
            location.href = "/devices/";
        },

    });
}

function userToggle(userId) {
    $.ajax({
        type:"POST",
        url:"/api/user/toggle/",
        data:{id:userId},
        success:function() {location.reload();},

    });
}

function showZoneAssignment(devId) {
    window.location = "/assign/" + devId + "/";
}

function requestSuperCookie() {
    getDevKey();
    $("#requestSuperCookie").prop('disabled', true);
    if ( devKey === "") {
        console.log(devKey);
        $("#requestSuperCookie").text("error.")
    } else {
        Cookies.set("DEV_KEY",devKey);
        $("#requestSuperCookie").text("Done.")
    }
}


function getDevKey() {
    var url = window.location.pathname;

    var devId = url.split("/")[2];
    if ( devId !== "" ) {
    $.get("/api/device/info/" ,  { id:devId }   ).done(function(data){
        if ( data.devType == "1" ) {
            devKey = data.devKey;

            $("#requestSuperCookie").show()
            if (Cookies.get("DEV_KEY") != data.devKey ) {
                $("#error").text( "Warning, current browser key is not matching our records.You will not be able to timestamp with this browser." )
            }

        } else {
            $("#requestSuperCookie").hide()

        }
    }).fail(function(error) {
        console.log("Unable to retreive key :(HTTP_" + error.status + ")");
    });
    } else {

        console.log("unable to get devId ");
    }
}

var devKey = "";
$(document).ready(function() {
    var devKey = "";
    setUpCSRFHeader();
    getDevKey();
});
